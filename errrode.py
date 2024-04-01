import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('C:\\Users\\ADMIN\\Downloads\\download.jpeg')

# Check if image is successfully loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply erosion
    kernel = np.ones((5,5), np.uint8)  # Define erosion kernel
    eroded_image = cv2.erode(gray_image, kernel, iterations=1)

    # Display original and eroded images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(eroded_image, cmap='gray')
    plt.title('Eroded Image')
    plt.axis('off')

    plt.show()
