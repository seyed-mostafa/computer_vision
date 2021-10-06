import cv2
import numpy as np
import matplotlib.pyplot as plt


def avg_brightness(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    sum_brightness = np.sum(hsv[:, :, 2])
    area = hsv.shape[0] * hsv.shape[1]
    avg = sum_brightness / area
    return avg


def day_or_night(image):
    if avg_brightness(image) < 100:
        return 0
    return 1


while True:
    input_dir = input('input directory : ')
    image = plt.imread('image/' + input_dir + '.jpg')

    if day_or_night(image) == 0:
        print('night')
    else:
        print('day')
