import cv2
import numpy as np

# 读取图像
img = cv2.imread('IMG_20190824_125459.jpg')
l = cv2.pyrDown(img)
l = cv2.pyrUp(l)
res = img - l
res = cv2.resize(res, (0, 0), fx=0.2, fy=0.2)
cv2.imshow('Contours', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
