import cv2
import time

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(1)
    time.sleep(5)
    while True:
        ret_val,img= cam.read()
        if mirror:
            img=cv2.flip(img, 1)
        cv2.imshow('Mywebcam', img)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ =='__main__':
    main()
