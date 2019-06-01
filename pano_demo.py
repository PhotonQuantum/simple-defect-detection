import cv2
import imutils
from panorama import Stitcher
import numpy as np


def sharpen(img):
    kern = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(img, -1, kern)


a = cv2.imread("frames/002.jpg")
b = cv2.imread("frames/003.jpg")

a = sharpen(a)
b = sharpen(b)

stitcher = Stitcher()
(result, vis) = stitcher.stitch([a, b], showMatches=True)

cv2.imshow("a", vis)
cv2.waitKey(0)
cv2.imshow("a", result)
cv2.waitKey(0)
cv2.imwrite("vis.jpg", vis)
cv2.imwrite("res.jpg", result)
