import cv2
import numpy as np
import sys


def main():
    im = cv2.imread(sys.argv[1])
    r = cv2.selectROI(im)
    print(r)


if __name__ == '__main__':
    main()
