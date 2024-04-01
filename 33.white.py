import cv2 
path = r'C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg'
image = cv2.imread(path, 0) 
window_name = 'Image'
start_point = (100, 50) 
end_point = (125, 125) 
color = (255, 255, 255) 
thickness = -1
image = cv2.rectangle(image, start_point, end_point, color, thickness) 
cv2.imshow(window_name, image) 
cv2.waitKey(0)