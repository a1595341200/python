import cv2
import numpy as np

# 读取图像
img = cv2.imread('vscode.png', cv2.IMREAD_GRAYSCALE)
# 二值化处理
_, img = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)

# 轮廓检测
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 绘制轮廓
imgcpoy = img.copy()
res = cv2.drawContours(imgcpoy, contours, -1, (0, 0, 255), 3)

# 显示图像
cv2.imshow('Contours', imgcpoy)
cv2.waitKey(0)
cv2.destroyAllWindows()
