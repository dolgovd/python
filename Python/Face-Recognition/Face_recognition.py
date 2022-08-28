# Program allows to detect faces in video stream. Connected devices or video file can be used as input
# Library "opencv-python" is used
# Documnetation: https://docs.opencv.org/3.4/
# github: https://github.com/opencv/opencv/tree/master
# filters: https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

def face_capture():
    cascase_path = '/Users/ddolgov/Git/single-repo/Python/Face-Recognition/filters/haarcascade_frontalface_default.xml'

    # Create an object
    clf = cv2.CascadeClassifier(cascase_path)

    # Capture video stream and select source (device id or name of video file)
    camera = cv2.VideoCapture('video.mp4')

    while True:
        # Catch the next frame
        _, frame = camera.read()

        # Move each frame to grayscale mode for better quality of recognition
        gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Looking for faces
        faces = clf.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        # Show faces in frames
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
        
        cv2.imshow('Faces', frame)

        # Stop the program in case of demand
        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
     
def main():
    face_capture()

if __name__ == '__main__':
    main()