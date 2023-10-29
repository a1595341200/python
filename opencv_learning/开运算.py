import cv2
import numpy as np

# 读取图像
img = cv2.imread('IMG_20190824_125459.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
# 定义结构元素
kernel = np.ones((3, 3), np.uint8)

# 进行开运算
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 显示图像
cv2.imshow('Original Image', img)
cv2.imshow('Opening Image', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()