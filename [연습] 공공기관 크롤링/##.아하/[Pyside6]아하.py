from PySide6.QtWidgets import QApplication, QWidget
from aha import Ui_Form
import sys
import requests 
from bs4 import BeautifulSoup
import pandas as pd


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())

