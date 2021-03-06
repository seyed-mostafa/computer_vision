
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import imutils


# Load our image
binary_warped = mpimg.imread('warped-example.jpg')
#np.set_printoptions(threshold=np.inf)

#
# left_fit = np.array([2.13935315e-04, -3.77507980e-01, 4.76902175e+02])
# right_fit = np.array([4.17622148e-04, -4.93848953e-01, 1.11806170e+03])
#
#
# def fit_poly(img_shape, leftx, lefty, rightx, righty):
#     left_fit = np.polyfit(lefty, leftx, 2)
#     right_fit = np.polyfit(righty, rightx, 2)
#     ploty = np.linspace(0, img_shape[0] - 1, img_shape[0])
#     left_fitx = left_fit[0] * ploty ** 2 + left_fit[1] * ploty + left_fit[2]
#     right_fitx = right_fit[0] * ploty ** 2 + right_fit[1] * ploty + right_fit[2]
#
#     return left_fitx, right_fitx, ploty
#
#
# def search_around_poly(binary_warped):
#     margin = 100
#     nonzero = binary_warped.nonzero()
#     nonzeroy = np.array(nonzero[0])
#     nonzerox = np.array(nonzero[1])
#     left_lane_inds = ((nonzerox > (left_fit[0] * (nonzeroy ** 2) + left_fit[1] * nonzeroy +
#                                    left_fit[2] - margin)) & (nonzerox < (left_fit[0] * (nonzeroy ** 2) +
#                                                                          left_fit[1] * nonzeroy + left_fit[
#                                                                              2] + margin)))
#     right_lane_inds = ((nonzerox > (right_fit[0] * (nonzeroy ** 2) + right_fit[1] * nonzeroy +
#                                     right_fit[2] - margin)) & (nonzerox < (right_fit[0] * (nonzeroy ** 2) +
#                                                                            right_fit[1] * nonzeroy + right_fit[
#                                                                                2] + margin)))
#
#     leftx = nonzerox[left_lane_inds]
#     lefty = nonzeroy[left_lane_inds]
#     rightx = nonzerox[right_lane_inds]
#     righty = nonzeroy[right_lane_inds]
#     left_fitx, right_fitx, ploty = fit_poly(binary_warped.shape, leftx, lefty, rightx, righty)
#     out_img = np.dstack((binary_warped, binary_warped, binary_warped)) * 255
#     window_img = np.zeros_like(out_img)
#     out_img[nonzeroy[left_lane_inds], nonzerox[left_lane_inds]] = [255, 0, 0]
#     out_img[nonzeroy[right_lane_inds], nonzerox[right_lane_inds]] = [0, 0, 255]
#
#     left_line_window1 = np.array([np.transpose(np.vstack([left_fitx - margin, ploty]))])
#     left_line_window2 = np.array([np.flipud(np.transpose(np.vstack([left_fitx + margin,
#                                                                     ploty])))])
#     left_line_pts = np.hstack((left_line_window1, left_line_window2))
#     right_line_window1 = np.array([np.transpose(np.vstack([right_fitx - margin, ploty]))])
#     right_line_window2 = np.array([np.flipud(np.transpose(np.vstack([right_fitx + margin,
#                                                                      ploty])))])
#     right_line_pts = np.hstack((right_line_window1, right_line_window2))
#
#     cv2.fillPoly(window_img, np.int_([left_line_pts]), (0, 255, 0))
#     cv2.fillPoly(window_img, np.int_([right_line_pts]), (0, 255, 0))
#     result = cv2.addWeighted(out_img, 1, window_img, 0.3, 0)
#
#     plt.plot(left_fitx, ploty, color='yellow')
#     plt.plot(right_fitx, ploty, color='yellow')
#
#     return result
#
#
#
# result = search_around_poly(binary_warped)
#
# # View your output
# plt.imshow(result)
# plt.show()





def out(average_line):
    pass



def find_lane_pixels(binary_warped):
    # Take a histogram of the bottom half of the image
    histogram = np.sum(binary_warped[binary_warped.shape[0] // 2:, :], axis=0)
    # Create an output image to draw on and visualize the result
    out_img = np.dstack((binary_warped, binary_warped, binary_warped))
    # Find the peak of the left and right halves of the histogram
    # These will be the starting point for the left and right lines
    midpoint = int(histogram.shape[0] // 2)
    leftx_base = np.argmax(histogram[:midpoint])
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint

    # HYPERPARAMETERS
    # Choose the number of sliding windows
    nwindows = 30
    # Set the width of the windows +/- margin
    margin = 15
    # Set minimum number of pixels found to recenter window
    minpix = 20

    # Set height of windows - based on nwindows above and image shape
    window_height = int(binary_warped.shape[0] // nwindows)
    # Identify the x and y positions of all nonzero pixels in the image
    nonzero = binary_warped.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])

    # Current positions to be updated later for each window in nwindows
    leftx_current = leftx_base
    rightx_current = rightx_base

    # Create empty lists to receive left and right lane pixel indices
    left_lane_inds = []
    right_lane_inds = []

    # Step through the windows one by one
    for window in range(nwindows):
        # Identify window boundaries in x and y (and right and left)
        win_y_low = binary_warped.shape[0] - (window + 1) * window_height
        win_y_high = binary_warped.shape[0] - window * window_height
        win_xleft_low = leftx_current - margin
        win_xleft_high = leftx_current + margin
        win_xright_low = rightx_current - margin
        win_xright_high = rightx_current + margin

        # Draw the windows on the visualization image
        cv2.rectangle(out_img, (win_xleft_low, win_y_low),
                      (win_xleft_high, win_y_high), (0, 255, 0),2)
        cv2.rectangle(out_img, (win_xright_low, win_y_low),
                      (win_xright_high, win_y_high), (0, 255, 0), 2)

        # Identify the nonzero pixels in x and y within the window #
        good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
                          (nonzerox >= win_xleft_low) & (nonzerox < win_xleft_high)).nonzero()[0]
        good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
                           (nonzerox >= win_xright_low) & (nonzerox < win_xright_high)).nonzero()[0]

        # Append these indices to the lists
        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)

        # If you found > minpix pixels, recenter next window on their mean position
        if len(good_left_inds) > minpix:
            leftx_current = int(np.mean(nonzerox[good_left_inds]))
        if len(good_right_inds) > minpix:
            rightx_current = int(np.mean(nonzerox[good_right_inds]))

    # Concatenate the arrays of indices (previously was a list of lists of pixels)
    try:
        left_lane_inds = np.concatenate(left_lane_inds)
        right_lane_inds = np.concatenate(right_lane_inds)
    except ValueError:
        # Avoids an error if the above is not implemented fully
        pass

    # Extract left and right line pixel positions
    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds]
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds]


    return leftx, lefty, rightx, righty, out_img


def fit_polynomial(binary_warped):
    # Find our lane pixels first
    leftx, lefty, rightx, righty, out_img = find_lane_pixels(binary_warped)

    # Fit a second order polynomial to each using `np.polyfit`
    left_fit = np.polyfit(lefty, leftx,2)
    right_fit = np.polyfit(righty, rightx, 2)

    # Generate x and y values for plotting
    ploty = np.linspace(0, binary_warped.shape[0] - 1, binary_warped.shape[0])
    try:
        left_fitx = left_fit[0] * ploty ** 2 + left_fit[1] * ploty + left_fit[2]
        right_fitx = right_fit[0] * ploty ** 2 + right_fit[1] * ploty + right_fit[2]
    except TypeError:
        # Avoids an error if `left` and `right_fit` are still none or incorrect
        print('The function failed to fit a line!')
        left_fitx = 1 * ploty ** 2 + 1 * ploty
        right_fitx = 1 * ploty ** 2 + 1 * ploty


    average_line = np.mean(np.array([left_fitx,right_fitx]),axis=0)


    # Plots the left and right polynomials on the lane lines
    plt.plot(left_fitx, ploty, color='yellow')
    plt.plot(right_fitx, ploty, color='yellow')
    plt.plot(average_line, ploty, color='red')

    # print(ploty)
    # plt.imshow(out_img)
    # plt.show()

    #return out_img
    #return average_line
    return ((left_fitx[-1] + right_fitx[-1]) / 2) * 1280 / 215



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
        out_img = fit_polynomial(processed_frame)
        plt.imshow(frame)
        plt.show()

    #     cv2.imshow('video', out_img)
    #     if cv2.waitKey(1) == 27:
    #         break
    # else:
    #     break
video.release()
cv2.destroyAllWindows()