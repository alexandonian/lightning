import sys
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd
from PIL import Image as Pimage
from skimage import util
from image import Image
import readers as reader
from ..readers import *
from ..resources.values import Types, Paths, Project_info


class ImageProvider(object):
    """Generate and handle Image object

    The ImageProvider (and ImageSetProvider) class bridge the gap between
    ImageSet and Image objects. For each image in an imageset, an ImageProvider
    is dispatched to generate an Image object. The ImageSetProvider passes
    path and metadata information for all imaging modalities to the
    ImageProvider, which loads images and features. Lastly, the ImageProvider
    also generates labels that index and Image object's image array.

    """

    def __init__(self, image_info):
        """Initialize ImageProvider object.

        :param image_info: a nested dictionary containing image and path info.
        The structure of image_info is shown below:

        image_info = {image_type:
                                 {'path_name': path_name},
                                 {'file_name': file_name},
                                 {'channel_list': channel_list}
                                 {'image_shape': image_shape}}

        where path_name = {'images': image_path
                           'features': features_path}
              file_name = {'images': image_name
                           'features': features_name}

        :return: an imageprovider

        """
        self.image_info = image_info
        self.image_name = self.determine_image_name(image_info)
        self.class_num = self.determine_class_num(image_info)
        self.feat_data = None
        self.image_obj = None
        self.patches = None

    def generate_image_obj(self):

        im_data = {}
        feat_data = {}

        self.image_obj = self.load_images_by_type('IF')
        for im_type in self.image_info.keys():
            #     self.image_obj = self.load_images_by_type(type)
            #     # im_data[im_type] = self.load_images_by_type(im_type)
            feat_data[im_type] = self.load_features_by_type(im_type)

        self.feat_data = feat_data

        # image_obj = Image(self.image_info, im_data, feat_data)

        # image_obj = Image(im_data[Strings.IF], self.image_info[Strings.IF]['channel_list'])
        # self.image_obj = image_obj
        # self.feat_data = feat_data

        return self.image_obj

    def load_images_by_type(self, im_type):

        if im_type == Types.IF:
            image_shape = self.image_info[Types.IF]['image_shape']
            im_paths = self.image_info[Types.IF]['path']['images']
            channel_list = self.image_info[Types.IF]['channel_list']
            return reader.fromtiflist(im_paths, labels=channel_list)
            # values = np.zeros((len(channel_list), image_shape[0], image_shape[1]))
            #
            # # return reader.fromlist(im_paths, self.frompath, labels=channel_list)
            # for i, path in enumerate(im_paths):
            #     with Pimage.open(path).convert('L') as im:
            #         im = np.array(im)
            #         values[i, :, :] = util.img_as_float(im)
            #
            # return values
        return None

    def load_features_by_type(self, im_type):

        # TODO: Refactor the following code into a separate function
        # e.g. if type == Strings.IF:
        #   fetcher = infoFetcher()
        #   feats = fetcher.fetch_IF_features
        # OR
        #   feats = fetcher.fetch_features(String.IF)
        #   further organization of features?
        #   Consult others?
        if im_type == Types.IF:

            feats = {'xy': None,
                     'intensity': None}

            feat_path = self.image_info[Types.IF]['path']['features'][0]
            df = pd.read_csv(feat_path)

            # Load spatial xy coordinates
            feats['xy'] = (
                np.concatenate((np.reshape(df.Cell_X, (-1, 1)),
                                np.reshape(df.Cell_Y, (-1, 1))), axis=1))

            # Based on column headers, read biomarker identities
            # and expression locations
            bio, loc, col = (
                zip(*[(col.split('_')[0], col.split('_')[1], col)
                      for col in list(df) if col.split('_')[0] != 'Cell']))

            # Extract a list of unique biomarkers and expression locations
            biomarkers = list(set(bio))
            locations = list(set(loc))

            # Load intensities for all channels and all locations
            k = 0
            intensity = {}
            # channels = self.image_info[Strings.IF]['channel_list']
            for bio in biomarkers:
                intensity[bio] = {}
                for loc in locations:
                    intensity[bio][loc] = df[col[k]].values
                    k += 1
            feats['intensity'] = intensity

            return feats
        return None

    def patchify(self, patch_shape=(256, 256, 3), overlap=0):
        #    if channel:
        #     im = self.images[channel]
        # else:
        #     im = self.images[Strings.IF]
        # # if patch_shape != im.shape: This doesn't make any sense!!!!
        # if path_shape
        #     patch_shape = (256, 256, im.shape[2])

        step = tuple((patch_shape[0] - overlap, patch_shape[1] - overlap, 1))
        im = self.image_obj.toarray()[0:3, :, :]
        im = np.swapaxes(im, 0, 2)
        patches = util.shape.view_as_windows(im, patch_shape, step)
        self.patches = patches

    @staticmethod
    def determine_image_name(type):
        return None

    @staticmethod
    def determine_class_num(type):
        return None

        ###########################################################################
        # FUTURE METHODS:
        # - coordinating alignment within a 2D plane for each image type
        # - coordinating alignment within a 2D plane across image types
        ###########################################################################


class ImageSetProvider(object):
    """Generate and dispatch ImageProvider objects.

    The ImageSet (and ImageProvider) class bridge the gap between
    ImageSet and Image objects. The ImageSetProvider determines the image
    modalities of interest, finds all image and data files for each image type
    and passes this information to individual ImageProviders, which generate
    image objects. For each image object, the ImageSetProvider passes one image
    and data file for all image types to an ImageProvider.

    """

    def __init__(self):
        """
        TODO: a list of imaging modalities OR a a dictionary containing
        imaging modalities mapped to their paths something like that
        for each imaging modality (given by values.py)
        determine the number of subchannels
        determine the number of images per subchannel
        for each subchannel image
          load image_info dictionary
        """

        self.project_info = Project_info

        if Project_info is not None:
            self.num_types = len(Project_info.keys())
        else:
            self.num_types = None
        self.num_images = None
        self.image_info_list = None

    def has_subchannels(self):
        pass

    def fetch_project_info(self):
        """
        TODO:
        Fetch information about the imaging modality such as features of
        interest, number of feature channels etc.

        Example, for multiplexed immunofluorescence imaging modality, we want
        to know:
        - features: biomarker intensity at xy locations
        - number of features: how many biomarkers are we interested in
        """

        # fetcher = infoHelper()
        # info = fetcher.fetch_IF_info('i')

        # FOR NOW: load manually from values.Project_info

    def fetch_image_info_list(self):

        # TODO:
        image_types = self.project_info.keys()

        im_info_list = None
        return im_info_list

    def fetch_features(self, modality, info):
        """
        TODO:
        """
        pass

        if modality == "IF":
            fetcher = featureHelper()
            features = fetcher.fetch_IF_features()

        return features


class ImageInfo(object):
    def __init__(self):
        pass

    @property
    def channel_list(self):
        return self.channel_list

    @property
    def subchannel_list(self):
        return self.subchannel_list

    @property
    def path(self):
        return self.path

    @property
    def file_name(self):
        return self.file_name


class Image_info(object):
    pass
    # TODO: migrate image_info dictionary to Image_info transaction object

    # path_to_images = ['resources/images/ER-allTissue/ER_AFRemoved_013.tif',
    #                   'resources/images/PR-allTissue/PR_AFRemoved_013.tif',
    #                   'resources/images/HER2-allTissue/Her2_AFRemoved_013.tif']
    # path_to_features = ['resources/data/013_Quant.csv']
    # channel_list = ['ER', 'PR', 'HER2']
    #
    # image_shape = (2048, 2048)
    # path = {'images': path_to_images,
    #         'features': path_to_features}
    # file_name = {'images': 'image_names',
    #              'feature': 'feature_name'}
    # im_type_info = {'path': path,
    #                 'file_name': file_name,
    #                 'channel_list': channel_list,
    #                 'image_shape': image_shape}
    #
    # image_info = {Strings.IF: im_type_info}


class infoHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def fetch_IF_info(param):
        if param == "i":
            print 'test'

    @staticmethod
    def fetch_WSI_info(param):
        pass

    @staticmethod
    def fetch_IHC_info(param):
        pass

    @staticmethod
    def fetch_HaE_info(param):
        pass

    @staticmethod
    def fetch_IMS_info(param):
        pass

    @staticmethod
    def fetch_ISH_info(param):
        pass


class featureHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def fetch_IF_info(param):
        if param == "i":
            print 'test'

    @staticmethod
    def fetch_WSI_features(param):
        pass

    @staticmethod
    def fetch_IHC_features(param):
        pass

    @staticmethod
    def fetch_HaE_features(param):
        pass

    @staticmethod
    def fetch_IMS_features(param):
        pass

    @staticmethod
    def fetch_ISH_features(param):
        pass


class imageHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def fetch_IF_info(param):
        if param == "i":
            print 'test'

    @staticmethod
    def fetch_WSI_image(param):
        pass

    @staticmethod
    def fetch_IHC_images(param):
        pass

    @staticmethod
    def fetch_HaE_images(param):
        pass

    @staticmethod
    def fetch_IMS_images(param):
        pass

    @staticmethod
    def fetch_ISH_images(param):
        pass
