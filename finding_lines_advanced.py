import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Load our image
# `mpimg.imread` will load .jpg as 0-255, so normalize back to 0-1
img = mpimg.imread("warped-example.jpg") / 255


def hist(img):
    bottom_half = img[img.shape[0] // 2:, :]
    histogram = np.sum(bottom_half)
    return histogram


histogram = np.sum(img[img.shape[0]//2:,:], axis=0)
plt.plot(histogram)
plt.show()