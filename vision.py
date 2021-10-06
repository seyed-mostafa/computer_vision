import numpy as np
import matplotlib.image as mpimg  # for reading in images
import matplotlib.pyplot as plt
import cv2

# image = mpimg.imread('images/wa_state_highway.jpg')
#
# #plt.imshow(image)
#
# # Isolate RGB channels
# r = image[:, :, 1]
# image[:, :, 0] = 0
# image[:, :, 2] = 0
#
# g = image[:, :, 1]
# b = image[:, :, 2]
#
# print(image[1100,3000 , 1])
#
# plt.imshow(b)
#
# # Visualize the individual color channels
# f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
# ax1.set_title('R channel')
# ax1.imshow(image)
# ax2.set_title('G channel')
# ax2.imshow(g, cmap='gray')
# ax3.set_title('B channel')
# ax3.imshow(b, cmap='gray')


######################################################################


image = cv2.imread('images/pizza_bluescreen.jpg')

# Print out the type of image data and its dimensions (height, width, and color)
print('This image is:', type(image),
      ' with dimensions:', image.shape)

# Make a copy of the image
image_copy = np.copy(image)

# Change color to RGB (from BGR)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Display the image copy
# plt.imshow(image_copy)
# plt.show()


lower_blue = np.array([0, 0, 235])
upper_blue = np.array([250, 250, 255])

mask = cv2.inRange(image_copy, lower_blue, upper_blue)

# Visualize the mask
plt.imshow(mask, cmap='gray')


masked_image = np.copy(image_copy)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)
plt.show()


