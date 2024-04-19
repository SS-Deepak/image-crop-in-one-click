import cv2
import urllib.request
import numpy as np


def url_to_image(image_url: str):
    # Fetch image data from URL
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    # Convert image data to numpy array
    image_array = np.frombuffer(image_data, np.uint8)

    # Decode image array using OpenCV
    return cv2.imdecode(image_array, cv2.IMREAD_COLOR)
