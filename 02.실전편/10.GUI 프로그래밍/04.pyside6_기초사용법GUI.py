# QApplication 은 어플리케이션 설정, 관리
# QWidget 은 qt에서 제공하는 기본 창 클래스 
# 로그인 ui_form 가져올거야
# 파이썬 sys 임포트함
from PySide6.QtWidgets import QApplication, QWidget
from login import Ui_Form
import sys


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.객체이름.clicked.connect(self.실행할메서드이름)
        self.login_btn.clicked.connect(self.login)

    def login(self):
        print(f"아이디 : {self.id.text()}")
        print(f"비밀번호 : {self.pw.text()}")
        

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())

