
import cv2
from helper import mouse_callback
from actions import Actions
from variables import main_window_name, image_url
from url_to_image import url_to_image
from get_webcam_image import get_webcam_image

# Load the image
image = url_to_image(image_url)
# image = get_webcam_image()


# Create a window and set the mouse callback function
cv2.namedWindow(main_window_name)
cv2.setMouseCallback(main_window_name, mouse_callback)


# action to perform
Actions(image)


# destroy all instances
cv2.destroyAllWindows()
