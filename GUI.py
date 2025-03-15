import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QDesktopWidget, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('实时检测')

        # 初始化中央部件
        self.central_widget = QWidget()  # 确保初始化了central_widget
        self.setCentralWidget(self.central_widget)

        # 布局
        self.layout = QGridLayout()  # 使用网格布局
        self.central_widget.setLayout(self.layout)

        # 视频显示标签
        self.video_label = QLabel()
        self.layout.addWidget(self.video_label, 0, 0)

        # 状态栏
        self.statusBar().showMessage('应用已启动')

        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()
        width = screen.width()
        height = screen.height()

        # 设置窗口大小为屏幕的80%
        self.setGeometry(0, 0, int(width * 0.5), int(height * 0.5))

        # YOLO模型初始化
        self.model = self.load_yolo_model('fruit_nano.pt')  # 加载YOLO模型
        self.statusBar().showMessage('模型加载完成')
        self.video_timer = QTimer()
        self.video_timer.timeout.connect(self.update_frame)

        # 启动视频捕捉
        self.cap = cv2.VideoCapture(0)  # 使用默认摄像头
        self.video_timer.start(20)  # 每20毫秒更新一次

    def load_yolo_model(self, model_path):
        from ultralytics import YOLO
        return YOLO(model_path)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        # YOLO推理
        results = self.model(frame, conf=0.5)  # 使用YOLO模型进行推理，可以通过调整 conf 设置置信度
        annotated_frame = results[0].plot()  # 绘制标注

        # 转换为QImage以便在QLabel中显示
        h, w, ch = annotated_frame.shape
        bytes_per_line = ch * w
        q_img = QImage(annotated_frame.data, w, h, bytes_per_line, QImage.Format_BGR888)
        self.video_label.setPixmap(QPixmap.fromImage(q_img))


    def closeEvent(self, event):
        """关闭窗口时释放摄像头"""
        self.cap.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
