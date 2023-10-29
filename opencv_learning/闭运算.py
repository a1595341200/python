import cv2
import numpy as np

# 读取图像
img = cv2.imread('IMG_20190824_125459.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
# 定义结构元素
kernel = np.ones((5, 5), np.uint8)

# 进行闭运算
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)

# 显示图像
cv2.imshow('Original Image', img)
cv2.imshow('Closing Image', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
