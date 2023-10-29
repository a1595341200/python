import cv2
import numpy as np

# 读取图像
img = cv2.imread('IMG_20190824_125459.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
# 计算x方向和y方向的梯度
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# 计算梯度幅度和方向
# gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)
# gradient_direction = np.arctan2(sobely, sobelx)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

gradient_magnitude = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# 显示结果
cv2.imshow('Original Image', img)
cv2.imshow('Gradient Magnitude', gradient_magnitude)
# cv2.imshow('Gradient Direction', gradient_direction)
cv2.imshow('Gradient sobelx', sobelx)
cv2.imshow('Gradient sobely', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
