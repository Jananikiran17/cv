import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\ADMIN\\Pictures\\wallpaper\\skull.jpg')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corners = cv2.cornerHarris(gray_image, 2, 3, 0.04)
corners = cv2.dilate(corners, None)
threshold = 0.01 * corners.max()
image[corners > threshold] = [0, 0, 255]  
cv2.imshow('Detected Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
