import cv2
import numpy as np
import utils


def update_pic(update):
    l_filter = np.array([cv2.getTrackbarPos('L:H', 'picker'), cv2.getTrackbarPos('L:S', 'picker'), cv2.getTrackbarPos('L:V', 'picker')])
    u_filter = np.array([cv2.getTrackbarPos('U:H', 'picker'), cv2.getTrackbarPos('U:S', 'picker'), cv2.getTrackbarPos('U:V', 'picker')])
    print(l_filter)
    print(u_filter)
    mask = utils.hsv_mask(img, (l_filter, u_filter))
    mask = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations = cv2.getTrackbarPos('Erode iter:', 'picker'))
    mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations = cv2.getTrackbarPos('Dilate iter:', 'picker'))
    cnts, hi = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    out = img.copy()
    out = cv2.drawContours(out, cnts, -1, (0, 255, 0), 10)
    out = cv2.resize(out, (0, 0), fx=0.3, fy=0.3)
    cv2.imshow('picker', out)


img = cv2.imread("out.jpg")
cv2.namedWindow('picker')

cv2.createTrackbar('L:H', 'picker', 0, 180, update_pic)
cv2.createTrackbar('L:S', 'picker', 0, 255, update_pic)
cv2.createTrackbar('L:V', 'picker', 0, 255, update_pic)

cv2.createTrackbar('U:H', 'picker', 0, 180, update_pic)
cv2.createTrackbar('U:S', 'picker', 0, 255, update_pic)
cv2.createTrackbar('U:V', 'picker', 0, 255, update_pic)

cv2.createTrackbar('Erode iter:', 'picker', 0, 5, update_pic)
cv2.createTrackbar('Dilate iter:', 'picker', 0, 5, update_pic)

while True:
    if cv2.waitKey(10) & 0xFF == 27: break
cv2.destroyAllWindows()
