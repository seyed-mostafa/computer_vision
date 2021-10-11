import line_detection
import numpy as np
import cv2

image = cv2.imread("images/test_image.jpg")
lines = cv2.HoughLinesP(line_detection.region(line_detection.canny(image)), 10, np.pi / 180, 150, np.array([]), 20, 5)
averaged_lines = line_detection.average_slope_intercept(image, lines)
line_image = line_detection.display_line(image,averaged_lines)
combo_image = cv2.addWeighted(line_image,1,image,0.8,1)

cv2.imshow('video',combo_image)
cv2.waitKey()