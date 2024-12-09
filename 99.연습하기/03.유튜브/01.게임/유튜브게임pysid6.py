from PySide6.QtWidgets import QApplication, QWidget
from game import Ui_Form
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
        self.start_btn.clicked.connect(self.start) # 시작 버튼
        self.quit_btn.clicked.connect(self.quit) # 종료 버튼
        self.downLoad_btn.clicked.connect(self.downLoad) # 다운로드 버튼
        self.reset_btn.clicked.connect(self.reset) #리셋 버튼
        
    # 시작버튼
    def start(self):
        selected_text = self.comboBox.currentText()  # 현재 선택된 텍스트
        if selected_text== "게임":

            self.result.append("--- 크롤링 시작중입니다. 잠시만 기다리세요 ---")
            selected_text = self.comboBox.currentText()  # 현재 선택된 텍스트
            print(f"선택된 값: {selected_text}")
            
            URL = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

            # Chrome 옵션 설정 (브라우저 숨기기)
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # 브라우저를 백그라운드에서 실행
            options.add_argument("--disable-gpu")  # GPU 사용 안 함
            options.add_argument("--window-size=1920,1080")  # 화면 크기 설정
            options.add_argument("--disable-extensions")  # 확장 프로그램 비활성화
            options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화

            # 드라이버 생성
            driver = webdriver.Chrome(options=options)
            driver.get(URL)

            # 게임 카테고리 클릭
            catagoryGame = driver.find_element(By.CSS_SELECTOR, "#tabsContent > yt-tab-group-shape > div.yt-tab-group-shape-wiz__tabs > yt-tab-shape:nth-child(3) > div.yt-tab-shape-wiz__tab")
            catagoryGame.click()

            # 페이지 스크롤
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.select(".text-wrapper.style-scope.ytd-video-renderer")

            self.results = []

            for item in items:
                title = item.select_one("#video-title").text
                link = "https://www.youtube.com" + item.select_one("#video-title").attrs['href']
                channel = item.select_one(".yt-simple-endpoint.style-scope.yt-formatted-string").text   
                channelLink = "https://www.youtube.com" + item.select_one(".yt-simple-endpoint.style-scope.yt-formatted-string").attrs['href']
                view = item.select_one(".inline-metadata-item.style-scope.ytd-video-meta-block").text.split("조회수")[1].replace("회", "")
                
                self.result.append(title)
                QApplication.processEvents()  # UI 업데이트 처리
                self.results.append([title, link, channel, channelLink, view])

            self.result.append("--- 크롤링 끝 ---")

            # 드라이버 종료
            driver.quit()

        elif selected_text == "영화":
            print("영화로 할거임")
    
    # 리셋버튼
    def reset(self):
        self.result.setText("")    

    # 종료버튼
    def quit(self):
        sys.exit()

    # 엑셀로 저장시키기
    def downLoad(self):
        categoryName = self.keyword_input.text()

        # 데이터 프레임 생성
        df = pd.DataFrame(self.results, columns=["제목" , "링크", "채널명", "채널링크", "조회수",])
        df.to_excel(f'{categoryName}.xlsx')


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())
