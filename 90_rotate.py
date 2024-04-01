import cv2

path ="C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg"
src = cv2.imread(path)
window_name = 'Image'

# Rotate the image by 90 degrees clockwise
rotated_image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display the rotated image
cv2.imshow(window_name, rotated_image)
cv2.waitKey(0)
