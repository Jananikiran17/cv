import cv2
im = cv2.imread('C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg')
cv2.imshow('org',im)
cv2.waitKey(0)
gr=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow('gr',gr)
cv2.waitKey(0)
cv2.destroyAllWindow()