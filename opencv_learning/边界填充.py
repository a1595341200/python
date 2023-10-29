import cv2

# 读取图像
img = cv2.imread('IMG_20190824_125459.jpg')
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
# 边界填充
top = bottom = left = right = 50
borderType = cv2.BORDER_CONSTANT
borderColor = (255, 255, 255)  # 白色填充
filledImg = cv2.copyMakeBorder(img, top, bottom, left, right, borderType, value=borderColor)

# 显示图像
cv2.imshow('Original Image', img)
cv2.imshow('Filled Image', filledImg)
cv2.waitKey(0)
cv2.destroyAllWindows()