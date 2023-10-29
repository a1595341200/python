import cv2

# 创建VideoCapture对象并读取视频文件
cap = cv2.VideoCapture('VID_20220226_143656.mp4')

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件")
    exit()
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 循环读取视频帧
while True:
    # 读取下一帧
    ret, frame = cap.read()

    # 如果读取成功，则ret为True，否则为False
    if not ret:
        break

        # 显示视频帧
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', image)

    # 等待用户按下 'q' 键退出
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # 释放VideoCapture对象并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
