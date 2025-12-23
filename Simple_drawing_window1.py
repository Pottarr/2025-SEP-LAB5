import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class SimpleDrawingWindow(QWidget):
    def __init__(self):
        super().__init__(None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.resize(600, 500)
        self.rabbit = QPixmap("images/rabbit-png.png")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QColor(0, 0, 0))
        painter.setBrush(QColor(0, 127, 0))
        painter.drawPolygon([
            QPoint(70, 100),
            QPoint(100, 110),
            QPoint(130, 100),
            QPoint(100, 150)
        ])

        painter.setPen(QColor(255, 127, 0))
        painter.setBrush(QColor(255, 127, 0))
        painter.drawPie(50, 150, 100, 100, 0, 180 * 16)

        painter.setBrush(QColor(100, 100, 255))
        painter.drawPolygon([
            QPoint(50, 200),
            QPoint(150, 200),
            QPoint(100, 350)
        ])

        painter.setPen(QColor(0, 0, 255))
        painter.setBrush(QColor(150, 200, 255))
        painter.drawEllipse(200, 50, 100, 100)

        painter.setPen(QColor(150, 0, 0))
        painter.setBrush(QColor(255, 150, 150))
        painter.drawRect(200, 180, 140, 80)

        painter.setPen(QPen(QColor(0, 0, 0), 3))
        painter.drawLine(200, 300, 340, 360)

        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont("Arial", 14))
        painter.drawText(50, 420, "Hello from PySide6 🎨")

        painter.drawPixmap(QRect(380, 100, 180, 180), self.rabbit)

        painter.end()


def main():
    app = QApplication(sys.argv)
    w = SimpleDrawingWindow()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())


