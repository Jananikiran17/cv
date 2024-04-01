import cv2

path = "C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg"
src = cv2.imread(path)
window_name = 'Image'
flipped_image = cv2.flip(src, flipCode=0)  
rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name, rotated_image)
cv2.waitKey(0)
