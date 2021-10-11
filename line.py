import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils

def input_gray_image(path):
    image = cv2.imread(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image

def make_coordinates(image,line_parameters):
    slope,intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*3/5)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1,y1,x2,y2])

def average_slope_intercept(image,lines):
    left_fit, right_fit = [],[]
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1,x2),(y1,y2),1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    right_line = make_coordinates(image,right_fit_average)
    left_line = make_coordinates(image,left_fit_average)
    return np.array([left_line,right_line])


src = input_gray_image("images/test_image.jpg")
image = cv2.imread("images/test_image.jpg")
lines = cv2.HoughLinesP(region(canny(src)), 2, np.pi/180,100,np.array([]),40,5)
averaged_lines = average_slope_intercept(src, lines)
line_image = display_line(image,averaged_lines)
combo_image = cv2.addWeighted(line_image,1,image,0.8,1)


cv2.imshow('combo image',combo_image)
cv2.waitKey(0)
