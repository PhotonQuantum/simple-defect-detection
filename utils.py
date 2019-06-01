import cv2
import numpy as np


def hsv_mask(img, filter):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.inRange(hsv, filter[0], filter[1])

