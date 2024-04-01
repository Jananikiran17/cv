import cv2

def segment_image(input_image_path, lower_threshold, upper_threshold):
    # Read the input image
    input_image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to segment the image
    _, segmented_image = cv2.threshold(grayscale_image, lower_threshold, upper_threshold, cv2.THRESH_BINARY)

    # Display the original and segmented images
    cv2.imshow('Original Image', input_image)
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_image_path = 'C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg'
lower_threshold = 100
upper_threshold = 255
segment_image(input_image_path, lower_threshold, upper_threshold)
