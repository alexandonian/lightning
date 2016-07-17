import matplotlib.pyplot as plt
import numpy as np


def show_first_three_channels(image):
    if image.value_shape[0] > 3:
        im = image.toarray()[0:3, :, :]
        im = np.swapaxes(im, 0, 2)
        plt.imshow(im)
    else:
        plt.imshow(np.swapaxes(image.toarray(), 0, 2))
    plt.show()


def show_channel(channel):
    plt.imshow(channel)
    plt.show()


def show_subset_patches(patches, subplot_shape, channel_num=None):
    k = 1
    for i in range(subplot_shape[0]):
        for j in range(subplot_shape[1]):
            plt.subplot(subplot_shape[0], subplot_shape[1], k)
            if channel_num is not None:
                patch = patches[i, j, 0, :, :, channel_num]
            else:
                patch = patches[i, j, 0, :, :, :]
            plt.imshow(patch)
            cur_axes = plt.gca()
            cur_axes.axes.get_xaxis().set_visible(False)
            cur_axes.axes.get_yaxis().set_visible(False)
            k += 1
    plt.show()
