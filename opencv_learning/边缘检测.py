import cv2
import numpy as np

video = cv2.VideoCapture('VID_20220226_143656.mp4')

if video.isOpened():
    while True:
        res, img = video.read()
        if not res:
            break

        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        # 使用Canny算法进行边缘检测
        edges = cv2.Canny(image, 100, 300)

        # 显示原始图像和边缘检测结果
        merge = np.hstack((image, edges))
        cv2.imshow('Edge Detected Image', merge)
        cv2.waitKey(25)
video.release()
cv2.destroyAllWindows()
