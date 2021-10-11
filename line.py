import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils

def input_gray_image(path):
    image = cv2.imread(path)
    return image

def canny(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return imutils.auto_canny(blur, sigma=0.33)

def region(image):
   height = image.shape[0]
   triangle = np.array([[(200,height),(1100,height),(550,250)]])
   mask = np.zeros_like(image)
   cv2.fillPoly(mask,triangle,255)
   return cv2.bitwise_and(image,mask)

def display_line(image,lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
    return line_image


src = input_gray_image("images/test_image.jpg")
lines = cv2.HoughLinesP(region(canny(src)), 2, np.pi/180,100,np.array([]),40,5)

line_image = display_line(src,lines)
combo_image = cv2.addWeighted(line_image,0.8,src,1,1)


cv2.imshow('combo image',combo_image)
cv2.waitKey(0)
