import cv2

import eigenfaces
import gfx
from eigenfaces import EigenFaces

KEY_ESC = 27
count_captures = 0
count_timer = 0


def capture():
    vc = cv2.VideoCapture(0)
    if vc.isOpened():


        _, frame = vc.read()
        return gfx.Image(frame)


def display():
    vc = cv2.VideoCapture(0)
    key = 0
    success = True

    face_detector = gfx.FaceDetector()

    while success and key != KEY_ESC:
        success, frame = vc.read()
        face_detector.show(gfx.Image(frame), wait=False)
        key = cv2.waitKey(20)