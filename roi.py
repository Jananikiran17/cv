import cv2
source_image = cv2.imread("C:\\Users\\ADMIN\\Pictures\\wallpaper\\skull.jpg")
start_row = 100
end_row = 300
start_col = 200
end_col = 400

# Crop the region of interest from the source image
cropped_roi = source_image[start_row:end_row, start_col:end_col]

# Create a copy of the cropped ROI
copied_roi = cropped_roi.copy()

# Define the location to paste the copied ROI into the source image
paste_row = 50
paste_col = 150

# Paste the copied ROI into the source image
source_image[paste_row:paste_row+copied_roi.shape[0], paste_col:paste_col+copied_roi.shape[1]] = copied_roi

# Display the source image with the cropped and pasted ROI
cv2.imshow("Source Image", source_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
