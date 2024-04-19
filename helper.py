
import cv2
from variables import clicked_point, main_window_name


def mouse_callback(event, x, y, flags, param):
    global clicked_point

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_point = (x, y)


def crop_image(size, clonedImage):
    global clicked_point

    if clicked_point is not None:
        (x, y) = clicked_point

        yStart = y-size if y-size > 0 else 0
        yEnd = y+size if y+size > 0 else 0
        xStart = x-size if x-size > 0 else 0
        xEnd = x+size if x+size > 0 else 0

        cropped_face = clonedImage[yStart: yEnd, xStart: xEnd]

        cv2.destroyWindow(main_window_name)
        cv2.imshow('Cropped Face', cropped_face)
        cv2.waitKey(0)
