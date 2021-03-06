from turtle import width

import cv2  # computer vision library
import imutils

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def canny(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    return imutils.auto_canny(blur, sigma=0.33)  # better way to canny images


def process_frame(image):

    cropped_img = image[3 * int(image.shape[0] / 5):image.shape[0]]

    tl, tr, br, bl = [150 + 385, 30], [1050 - 300, 30], [1170, 200], [120, 200]
    pts1 = np.float32([tl, tr, br, bl])

    width = int(np.sqrt(((tl[1] - tr[1]) ** 2) + (tl[0] - tr[0]) ** 2))
    height = int(np.sqrt(((tl[1] - bl[1]) ** 2) + (tl[0] - bl[0]) ** 2))

    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOut = cv2.warpPerspective(cropped_img, matrix, (width, height))

    return canny(imgOut)


video = cv2.VideoCapture('videos/project_video.mp4')

while video.isOpened():
    ret, frame = video.read()
    if frame is not None:
        processed_frame = process_frame(frame)
        cv2.imshow('video', processed_frame)
        if cv2.waitKey(45) == 27:
            break
    else:
        break
video.release()
cv2.destroyAllWindows()






