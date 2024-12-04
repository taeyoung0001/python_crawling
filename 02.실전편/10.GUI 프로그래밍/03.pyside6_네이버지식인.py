# QApplication 은 어플리케이션 설정, 관리
# QWidget 은 qt에서 제공하는 기본 창 클래스 
# 로그인 ui_form 가져올거야
# 파이썬 sys 임포트함
from PySide6.QtWidgets import QApplication, QWidget
from naver_kin import Ui_Form
import sys
import requests 
from bs4 import BeautifulSoup
import pandas as pd


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.객체이름.clicked.connect(self.실행할메서드이름)
        self.start_btn.clicked.connect(self.start)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.quit_btn.clicked.connect(self.quit)

    def start(self):
        # 지식인의 키워드랑, 페이지의 변수 지정
        input_keyword = self.keyword.text()
        input_page = int(self.page.text())

        #result를 속성으로 만들어서 저장한다.
        self.result = []    
        for i in range(1, input_page + 1) :
            #텍스트 브라우저에 주입 방법(로딩중)
            self.textBrowser.append(f"---- {i} 페이지 크롤링----")

            response = requests.get(f"https://kin.naver.com/search/list.naver?query={input_keyword}&page={i}")
            html = response.text
            soup = BeautifulSoup(html , 'html.parser')
            items = soup.select('.basic1 > li ')
            for item in items :
                    
                title = item.select_one('._nclicks\\:kin\\.txt._searchListTitleAnchor').text
                link = item.select_one('._nclicks\\:kin\\.txt._searchListTitleAnchor').attrs['href']
                date = item.select_one('.txt_inline').text
                category = item.select_one(".txt_g1._nclicks\\:kin\\.cat2").text
                review = item.select_one('.hit').text.replace("답변수" , "").strip()

                #텍스트 브라우저에 주입 방법(실제 주입)
                self.textBrowser.append(title)
                
                #이벤트를 강제로 발생하게 해서 부드럽게 나오는거 표현
                QApplication.processEvents()

                #저장할 값 공간
                self.result.append([title, link,date, category, review])

            self.textBrowser.append("--- 크롤링 끝 ---")
            
    def reset(self):
        self.keyword.setText("")
        self.page.setText("")
        self.textBrowser.setText("")

    def save(self):
        # 키워드를 먼저 받아온다
        input_keyword = self.keyword.text()

        # 데이터 프레임 생성
        df = pd.DataFrame(self.result, columns=["제목" , "링크", "날짜", "카테고리", "리뷰 순"])
        df.to_excel(f'{input_keyword}.xlsx')
    def quit(self):
        sys.exit()
  
app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())

