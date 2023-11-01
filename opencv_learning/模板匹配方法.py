import cv2
import numpy as np

# 加载原图像和模板图像
image = cv2.imread('desktop.png')
t = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.png', cv2.IMREAD_GRAYSCALE)
# 获取模板图像的尺寸
print(template.shape)
w, h = template.shape[::-1]

# 使用模板匹配方法对原图像进行匹配
result = cv2.matchTemplate(t, template, cv2.TM_CCOEFF_NORMED)

# 设定阈值
threshold = 0.8

# 使用阈值筛选匹配结果
loc = np.where(result >= threshold)

# 在原图像中标出匹配区域
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
# 显示结果图像
cv2.imshow('Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
