import matplotlib.pyplot as plt
import numpy as np


def show(image):
    if image.value_shape[0] > 3:
        im = image.toarray()[0:3, :, :]
        im = np.swapaxes(im, 0, 2)
        plt.imshow(im)
    else:
        plt.imshow(np.swapaxes(image.toarray(), 0, 2))
    plt.show()


def show_subset_patches(patches, subplot_shape):
    k = 1
    for i in range(subplot_shape[0]):
        for j in range(subplot_shape[1]):
            plt.subplot(subplot_shape[0], subplot_shape[1], k)
            patch = patches[i, j, 0, :, :, :]
            plt.imshow(patch)
            k += 1
    plt.show()
