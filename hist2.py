import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate histogram
    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

    # Plot histogram
    plt.figure(figsize=(8, 5))
    plt.plot(hist, color='black')
    plt.title('Histogram of Grayscale Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Example usage:
image_path = 'C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg'
analyze_histogram(image_path)
