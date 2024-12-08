import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMessageBox, QStackedWidget, QTableWidgetItem

from ui_login import Ui_MainWindow as Login_UI
from ui_main import Ui_MainWindow as Main_UI

class Main_window(QMainWindow, Main_UI):
    def __init__(self):
        super(Main_window, self).__init__()
        self.setupUi(self)

        self.user_id:""
        self.user_pw:""
        self.current_keyword = ""
        self.keyword_list= []

        self.naver_id.textChanged.connect(self.change_id)
        self.naver_pw.textChanged.connect(self.change_pw)

        self.keyword_input.textChanged.connect(self.change_keyword)


        self.keyword_add_btn.clicked.connect(self.add_keyword)
        self.keyword_delet_btn.clicked.connect(self.delet_keyword)   
        self.process_start.clicked.connect(self.start_process)

    def change_id(self, text):
        self.user_id = text

    def change_pw(self, text):
        self.user_pw = text

    def show_dialog(self,title,msg):
        msgBox = QMessageBox()
        #i 아이콘
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def start_process(self):
        print("프로그램 동작 실행")
        print(self.user_id, self.user_pw)
    
    def change_keyword(self,text):
        self.current_keyword = text
        print(text)

    def add_keyword(self):
        # 만약 키워드의 길이가 1보다 작다면 코드를 실행하면 안됨
        if len(self.current_keyword) < 1:
            self.show_dialog("키워드를 입력해주세요" , "키워드의 길이는 1글자 이상이여야합니다.")
            #1글자 이하여도 추가가 되어서 return으로 디버깅~
            return
        currentRowCount = self.keyword_table.rowCount() #현재 테이블에 몇 개의 아이템이 들어가는지 return
        self.keyword_table.insertRow(currentRowCount)
        self.keyword_table.setItem(currentRowCount, 0 ,QTableWidgetItem(self.current_keyword))
        print(currentRowCount)

        # 키워드 리스트에 현재 테이블에 추가된 키워드 값을 추가해줄 것
        if len(self.keyword_list) == currentRowCount:
            # 삭제가 안된경우
            self.keyword_list.append(self.current_keyword)
        else:
            # 인덱스 꼬인경우
            self.keyword_list[currentRowCount] = self.current_keyword

        # UX를 고려한 키워드 인풋창 초기화
        self.keyword_input.clear()
        self.current_keyword = ""

class Login_window(QMainWindow, Login_UI):
    def __init__(self):
        super(Login_window, self).__init__()
        self.setupUi(self)
        self.userId =None
        self.userPw =None

        # 코드로 비밀번호 처리하기
        self.account_pw.setEchoMode(QLineEdit.EchoMode.Password)

         # ui적인거 코드로 만들기
        logo_pixmap = QPixmap('./logo.PNG')
        logo_pixmap = logo_pixmap.scaled(50, 41)

       
        self.main_logo.setPixmap(logo_pixmap)
        self.setWindowTitle("월천무기 서이주 프로그램")
        self.setWindowIcon(QIcon('./logo.PNG'))
        self.setFixedSize(250,350)

        # 기능 구현
        self.login_btn.clicked.connect(self.login_btn_clicked)

        self.account_id.textChanged.connect(self.change_id)

        self.account_pw.textChanged.connect(self.change_pw)

        self.blog_visit_btn.clicked.connect(self.open_blog_site)
    
    #링크이동
    def open_blog_site(self):
        import webbrowser
        webbrowser.open("http://naver.com")

    #로그인
    def login_btn_clicked(self):
        print("로그인 버튼이 클릭되었음")
        
        #서버에서 받은 로그인 성공, 실패 여부를 기반으로 메시지를 출력 or 화면 전환
        #서버 역할을 대신할 더미 데이터베이스를 만듦.
        User_Data = [["1","1"],["user2","4567"]]

        #로그인 성공 = 화면전환
        LOGIN_SUCCESS = False
        for user in User_Data:
            user_id, user_pw = user
            if self.userId == user_id and self.userPw == user_pw:
                print("로그인 성공")
                LOGIN_SUCCESS = True

                #메인화면으로 이동
                main_widget.setCurrentIndex(1)
                main_widget.setFixedSize(451,557)

               

        if LOGIN_SUCCESS:
            print("화면을 전환")

        #로그인 실패 = 에러 메시지
        else:
            print("에러 로직")
            self.show_dialog("로그인 실패", "로그인 실패 - 일치하는 계정 정보가 없습니다.")

    # 메세지 박스 띄워주기(alert 기능 같음)
    def show_dialog(self,title,msg):
        msgBox = QMessageBox()
        #i 아이콘
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)

        msgBox.exec()

     

    #id
    def change_id(self, text):
        self.userId = text

    #pw
    def change_pw(self, text):
        self.userPw = text


if __name__ == "__main__":
    app = QApplication(sys.argv)

    #화면 전환 
    main_widget = QStackedWidget()

    login_ui = Login_window()
    main_ui = Main_window()


    main_widget.addWidget(login_ui) 
    main_widget.addWidget(main_ui) 


    #화면 전환 방법 (idx로 스택으로 쌓이는 데 저 번호가 화면 숫자임)
    # main_widget.setCurrentIndex()
    main_widget.show()


    app.exec()