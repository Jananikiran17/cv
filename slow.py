import cv2

def manipulate_video_speed(video_path, speed_factor=1):
    video_capture = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(int(25 * speed_factor)) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

video_path = 'C:\\Users\\ADMIN\\Downloads\\walk.mp4'  
manipulate_video_speed(video_path)
manipulate_video_speed(video_path, 2)
manipulate_video_speed(video_path, 0.5)
