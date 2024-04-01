import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/ADMIN/Pictures/wallpaper/haarcascade_frontalface_default.xml')

image = cv2.imread('C:\\Users\\ADMIN\\Pictures\\Camera Roll\\WIN_20240327_12_38_02_Pro.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watches = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Detected Watches', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
