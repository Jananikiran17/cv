import cv2
import numpy as np

image = cv2.imread('C:\\Users\\ADMIN\\Pictures\\wallpaper\\skull.jpg', cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3) 
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Horizontal', sobel_x)
cv2.imshow('Sobel Vertical', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

