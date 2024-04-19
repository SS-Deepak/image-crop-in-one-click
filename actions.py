import cv2
from helper import crop_image
from variables import main_window_name


def Actions(image):
    clone = image.copy()

    while True:
        cv2.imshow(main_window_name, image)
        key = cv2.waitKey(1) & 0xFF

        if cv2.getWindowProperty(main_window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

        if key == ord('x'):
            crop_image(150, clone)
            break

        if key == ord('l'):
            crop_image(100, clone)
            break

        if key == ord('m'):
            crop_image(70, clone)
            break

        if key == ord('s'):
            crop_image(50, clone)
            break

        # If 'q' is pressed, quit
        elif key == ord('q'):
            break
