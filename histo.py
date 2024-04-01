import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg', 0)

# Apply histogram equalization
equalized_img = cv2.equalizeHist(img)

# Display original and equalized image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()
