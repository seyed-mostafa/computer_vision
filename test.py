from turtle import width

import cv2  # computer vision library

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = cv2.imread("images/test1.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

cropped_img = image[3*int(image.shape[0] /5) :image.shape[0]]

tl, tr, br, bl = [400+400,50], [1600-400,50],[1600,cropped_img.shape[0]], [400,cropped_img.shape[0]]
pts1 = np.float32([tl, tr, br, bl])
print(pts1)

width = int(np.sqrt(((tl[1] - tr[1])**2) + (tl[0] - tr[0])**2))
height = int(np.sqrt(((tl[1] - bl[1])**2) + (tl[0] - bl[0])**2))


pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(cropped_img,matrix,(width,height))

cv2.circle(cropped_img, (bl), 25, (255, 0, 0), cv2.FILLED)


plt.imshow(imgOut)
plt.show()



