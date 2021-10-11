import numpy as np
import matplotlib.pyplot as plt
import cv2

def input_gray_image(path):
    image = cv2.imread(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def canny(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region(image):
   height = image.shape[0]
   triangle = np.array([[(200,height),(1100,height),(550,250)]])
   mask = np.zeros_like(image)
   cv2.fillPoly(mask,triangle,255)
   return cv2.bitwise_and(image,mask)


src = input_gray_image("images/test_image.jpg")
cv2.imshow("region",region(canny(src)))
cv2.waitKey()

