from lightning.image.controller import ImageController, Provider
from lightning.image.image import Image
import lightning.image.readers as reader
from numpy import asarray
import matplotlib.pyplot as plt

test_path = 'resources/images/ER-allTissue/ER_AFRemoved_013.tif'
test_path2 = 'resources/images/ER-allTissue/'
tiflist = ['resources/images/ER-allTissue/ER_AFRemoved_013.tif', 'resources/images/PR-allTissue/PR_AFRemoved_013.tif',
           'resources/images/HER2-allTissue/Her2_AFRemoved_013.tif']
# im = reader.fromtif(test_path)
im = reader.fromtiflist(tiflist)
print(im)
# im = reader.frompathlist(test_path3)
# im = fromtif(tiflist)
# print(im)

import skimage.external.tifffile as tifffile
#
# arr = tifffile.imread(test_path)
# # print arr
#
# image = asarray([tifffile.imread(i) for i in tiflist])
# im = Image(image)
# print(im)
# print image.shape
# plt.imshow(image[0])
# plt.show()
