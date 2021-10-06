
# The first project that i coding
# this code will dropped a car and replace it in the sky!
#
# Good luck! :)

import cv2
import numpy as np
import matplotlib.pyplot as plt

car = plt.imread('images/car_green_screen.jpg')  # (450,660,3)
sky = plt.imread('images/sky.jpg')  # (575,1024,3)

lower_green = np.array([0, 150, 0])
upper_green = np.array([150, 256, 150])

mask = cv2.inRange(car, lower_green, upper_green)

masked_car = car.copy()
masked_car[mask != 0] = [0, 0, 0]

cropped_sky = sky[0:450, 0:660]
cropped_sky[mask == 0] = [0, 0, 0]

plt.imshow(cropped_sky + masked_car)
plt.show()
