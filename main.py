import cv2
import sys
import numpy as np
import utils

l_filter = np.array([70, 0, 120])
u_filter = np.array([90, 255, 255])
erode_iter = 1
dilate_iter = 1


def concat_pic(img1, img2):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((h1 + h2, max(w1, w2), 3), np.uint8)
    vis[:h1, :w1, :3] = img1
    vis[h1:h1 + h2, :w2, :3] = img2
    return vis


video = cv2.VideoCapture(sys.argv[1])
rtn, img = video.read()
if rtn:
    roi = list(cv2.selectROI("roi", img))
cv2.destroyWindow("roi")
count = 0
roi[1] = (roi[1] + roi[3]) // 2
roi[3] = 5
out = img[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]

print("Concating panorama...")
while rtn:
    rtn, img = video.read()
    if rtn:
        out = concat_pic(out, img[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]])
        if count % 10 == 0:
            cv2.imshow("cv", out)
            cv2.waitKey(1)
        count += 1
cv2.imwrite('out.jpg', out)
cv2.destroyWindow("cv")

print("HSV filtering...")
mask = utils.hsv_mask(out, (l_filter, u_filter))
mask = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=erode_iter)
mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=dilate_iter)
cnts, hi = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
out2 = out.copy()
out2 = cv2.drawContours(out2, cnts, -1, (0, 0, 255), 10)
# out2 = cv2.resize(out2, (0, 0), fx=0.3, fy=0.3)
cv2.imwrite('out2.jpg', out2)
out2 = cv2.resize(out2, (0, 0), fx=0.6, fy=0.6)
cv2.imshow('cvout', out2)
cv2.waitKey(0)
