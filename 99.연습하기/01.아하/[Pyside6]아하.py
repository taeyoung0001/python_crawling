from PySide6.QtWidgets import QApplication, QWidget
from aha import Ui_Form
import sys
from bs4 import BeautifulSoup
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 함수 지정
        self.start_btn.clicked.connect(self.start)
        self.quit_btn.clicked.connect(self.quit)
        self.downLoad_btn.clicked.connect(self.downLoad)
        self.reset_btn.clicked.connect(self.reset)

    # 추출하기(시작하기)
    def start(self):
        categoryName = self.keyword_input.text()
        detailCategoryName = self.detailCategory_input.text()
        scrollNumber = int(self.scroll_number.text())

        URL = f"https://www.a-ha.io/topic/{categoryName}/{detailCategoryName}"
        # 크롬 드라이버 생성
        driver = webdriver.Chrome()
        # 페이지 이동
        driver.get(URL)

        data = []

        # 스크롤 횟수
        # 현재 높이 가져오기
        last_height = driver.execute_script("return document.body.scrollHeight")
        for _ in range(scrollNumber + 1):
            # 스크롤 끝까지 내리기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            # 잠시 대기(컴퓨터에게 로딩 시간을 줘야 함)
            time.sleep(1)

            # 스크롤 후 높이 가져오기
            new_height = driver.execute_script("return document.body.scrollHeight")

            # 스크롤이 더 이상 내려가지 않으면 중단
            if new_height == last_height:
                break

            # 스크롤 전 높이 업데이트
            last_height = new_height 

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.select(".css-yd8sa2 > li")

        self.results = []
        for item in items:
            
            title = item.select_one(".css-1j6eql0.ecnp9of0").text
            category = item.select_one(".css-faq854.eblmy220").text
            detailCategory = item.select_one(".css-12osisl.ecnp9of0").text     
            content = item.select_one(".css-5z1n3l.eblmy220").text
            link = "https://www.a-ha.io/" + item.select_one("li > a").attrs["href"]
            answer = int(item.select_one(".css-16yaa9q.eblmy220").text.split("명")[0])
            

            self.result.append(title)
            QApplication.processEvents()
            self.results.append([title, category, detailCategory, content, link, answer])

        self.result.append("--- 크롤링 끝 ---")


    # 리셋하기
    # 함수로놔서 리셋 오류 계속 났다....
    def reset(self):
        self.keyword_input.setText("")
        self.detailCategory_input.setText("")
        self.scroll_number.setText("")
        self.result.setText("")


    # 엑셀로 저장시키기
    def downLoad(self):
        categoryName = self.keyword_input.text()

        # 데이터 프레임 생성
        df = pd.DataFrame(self.results, columns=["제목" , "카테고리", "상세분류", "내용", "링크", "전문가답변 순"])
        df.to_excel(f'{categoryName}.xlsx')

        

    # 종료하기
    def quit(self):
        sys.exit()

app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())

