from lightning.resources.values import Types
path_to_images = ['test/resources/images/ER-allTissue/ER_AFRemoved_013.tif',
                  'test/resources/images/PR-allTissue/PR_AFRemoved_013.tif',
                  'test/resources/images/HER2-allTissue/Her2_AFRemoved_013.tif']
path_to_features = ['test/resources/data/013_Quant.csv']
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




