import cv2
import numpy as np

# 读取图像
img = cv2.imread('IMG_20190824_125459.jpg')
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
img = cv2.pyrUp(img)
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
