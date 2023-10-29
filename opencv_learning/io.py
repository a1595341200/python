import cv2
import numpy as np
import matplotlib.pyplot as plt


def showImage(name, img):
    cv2.imshow(name, img)
    # 0 表示手动终止
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # 彩色
    img = cv2.imread('IMG_20190824_125459.jpg', cv2.IMREAD_COLOR)
    img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
    print(img)
    img = img + img
    cv2.imshow('test', img)
    # 0 表示手动终止
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 灰色
    img = cv2.imread('IMG_20190824_125459.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
    print(img)
    cv2.imshow('test', img)
    # 0 表示手动终止
    cv2.waitKey(0)
    cv2.destroyAllWindows()
