import cv2  # computer vision library
import helpers
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"

IMAGE_LIST = helpers.load_dataset(image_dir_training)

# Select an image and its label by list index

for image_index in range(240):
    selected_image = IMAGE_LIST[image_index][0]
    selected_label = IMAGE_LIST[image_index][1]
    print('The shape of the image: ', selected_image.shape,' ,and label is: ', selected_label)
    if selected_label == 'night':
        plt.imshow(selected_image)
        plt.show()




