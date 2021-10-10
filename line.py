
import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('images/test_image.jpg')
blur = cv2.GaussianBlur(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY),(5,5),0)
canny = cv2.Canny(blur,50,150)
cv2.imshow("canny picture",canny)
cv2.waitKey()

