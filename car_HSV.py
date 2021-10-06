
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


image = mpimg.imread('images/car_green_screen2.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

lower_hue = np.array([0,0,0])
upper_hue = np.array([97,255,255])

# Define the masked area
mask = cv2.inRange(image, lower_hue, upper_hue)

# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)
plt.show()