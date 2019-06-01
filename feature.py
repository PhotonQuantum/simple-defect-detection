import cv2

img = cv2.imread('out.jpg')
desc =cv2.xfeatures2d.SIFT_create()
(kps, features) = desc.detectAndCompute(img, None)
for kp in kps:
    pt = (int(kp.pt[0]), int(kp.pt[1]))
    img = cv2.circle(img, pt, int(kp.size), (0, 0, 255))
cv2.imshow("cv", img)
cv2.waitKey(0)
