import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, QtCore, QtGui
import socket
import cv2
import numpy as np

class DesktopCaptureApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Desktop Capture')

        self.label = QLabel(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.captureDesktop)
        self.timer.start(100)  # 100 ms interval

        # UDP Socket
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_address = ('10.44.89.147', 8888)

    def captureDesktop(self):
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)

        pixmap = QPixmap(screenshot)
        image = pixmap.toImage()

        # Convert QImage to numpy array
        img_array = np.array(image)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

        # Serialize the image
        _, img_encoded = cv2.imencode('.jpg', img_array)
        img_bytes = img_encoded.tobytes()

        # Send image via UDP
        self.udp_socket.sendto(img_bytes, self.udp_address)

        # Display the captured image
        self.label.setPixmap(pixmap)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.label.pixmap())

def main():
    app = QApplication(sys.argv)
    window = DesktopCaptureApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
