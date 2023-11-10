'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-11-09 11:58:20
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-11-09 11:58:20
FilePath: /python/video/recv.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import socket
import cv2
import numpy as np

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_address = ('127.0.0.1', 8888)

udp_socket.bind(udp_address)

while True:
    data, addr = udp_socket.recvfrom(65507)  # Adjust buffer size as needed
    img_array = np.frombuffer(data, dtype=np.uint8)

    # Decode and display the image
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    cv2.imshow('Received Image', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
