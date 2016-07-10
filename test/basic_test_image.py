from lightning import series, image
from lightning.image.controller import ImageController, ImageSetProvider
from lightning.image.readers import fromarray
from lightning.resources.values import Types
import numpy as np
from lightning_flash import image


path_to_images = ['resources/images/ER-allTissue/ER_AFRemoved_013.tif',
                  'resources/images/PR-allTissue/PR_AFRemoved_013.tif',
                  'resources/images/HER2-allTissue/Her2_AFRemoved_013.tif']
path_to_features = ['resources/data/013_Quant.csv']
channel_list = ['ER', 'PR', 'HER2']

image_shape = (2048, 2048)
path = {'images': path_to_images,
        'features': path_to_features}
file_name = {'images': 'image_names',
             'feature': 'feature_name'}
im_type_info = {'path': path,
                'file_name': file_name,
                'channel_list': channel_list,
                'image_shape': image_shape}

image_info = {Types.IF: im_type_info}

ip = ImageController(image_info)
im = ip.generate_image_obj()
print(im)
print('Labels: ')
print(im.labels)
print('Channels: ')
print(ip.channels)
print('Image types: ' + str(ip.feat_data.keys()))
print ('Features: ')
print(ip.feat_data['IF'].keys())
# ip.patchify(overlap=200)
# values = im.images[Strings.IF][:, :, :]
# values = np.append(values, np.ones((2048, 2048, 1)),axis=2)
# test = np.empty((1, 2048, 2048, 3))
# test[0,:, :, :] = values
# plt.imshow(im.images[Strings.IF][:, :, :])
# plt.show()



# image.show(im)
# image.show_subset_patches(ip.patches, (3, 3))

# plt.imshow(im[1, :, :])
# plt.show()
