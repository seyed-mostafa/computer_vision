import cv2  # computer vision library

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



image = cv2.imread("images/test_image.jpg")


cv2.imshow('image', image)
cv2.waitKey()