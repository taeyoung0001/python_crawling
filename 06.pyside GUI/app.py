import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
from PySide6.QtGui import QPixmap, QIcon
from ui_login import Ui_MainWindow

class Login_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Login_window, self).__init__()
        self.setupUi(self)

        # 코드로 비밀번호 처리하기
        self.account_pw.setEchoMode(QLineEdit.EchoMode.Password)
        logo_pixmap = QPixmap('./logo.PNG')
        logo_pixmap = logo_pixmap.scaled(50, 41)

        self.main_logo.setPixmap(logo_pixmap)
        self.setWindowTitle("월천무기 서이주 프로그램")
        self.setWindowIcon(QIcon('./logo.PNG'))
        self.setFixedSize(250,350)

app = QApplication(sys.argv)

window = Login_window()
window.show()

app.exec()