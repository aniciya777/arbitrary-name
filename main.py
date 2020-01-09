from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
import random
from PyQt5.QtGui import QPainter, QColor
import sys
from ui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.s_draw)
        self.is_draw = False

    def s_draw(self):
        self.is_draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        if self.is_draw:
            for i in range(25):
                rad = random.randint(0, 200)
                qp.setBrush(QColor(random.choice(['yellow', 'red', 'cyan', 'gray', 'black'])))
                qp.drawEllipse(random.randint(0, 420), random.randint(0, 410), rad, rad)
            self.is_draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    form = Form()
    form.show()
    sys.exit(app.exec())
