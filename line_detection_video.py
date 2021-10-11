import cv2
import numpy as np
import line_detection

def process_frame(image):
    lines = cv2.HoughLinesP(line_detection.region(line_detection.canny(image)), 10, np.pi / 180, 150, np.array([]), 20, 5)
    averaged_lines = line_detection.average_slope_intercept(image, lines)
    line_image = line_detection.display_line(image, averaged_lines)
    combo_image = cv2.addWeighted(line_image, 1, image, 0.8, 1)
    return combo_image


video = cv2.VideoCapture('videos/test2.mp4')
while video.isOpened():
    ret, frame = video.read()
    processed_frame = process_frame(frame)
    cv2.imshow('video',processed_frame)
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
