import numpy as np 
import cv2 

cap = cv2.VideoCapture('C:\\Users\\ADMIN\\Pictures\\wallpaper\\img.jpg') 
fgbg = cv2.createBackgroundSubtractorMOG2() 

while(1): 
	ret, frame = cap.read() 
	fgmask = fgbg.apply(frame) 

	cv2.imshow('fgmask', fgmask) 
	cv2.imshow('frame',frame ) 
	
	k = cv2.waitKey(0) & 0xff
	if k == 27: 
		break
	

cap.release() 
cv2.waitKey(0)
cv2.destroyAllWindows() 
