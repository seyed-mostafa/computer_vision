
import numpy as np
import matplotlib.pyplot as plt
import cv2

print()
image = cv2.imread('test_image.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()
