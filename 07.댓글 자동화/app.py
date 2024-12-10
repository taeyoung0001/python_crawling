from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pyperclip
import time


USER_ID = "her020212"
USER_PW = "Hh15300602!?!"

driver = webdriver.Chrome()

# URL 정리 (강의에서는 이렇게 안했는데, 난 이게 더 보기 좋다)
URL_NAVER = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com"
URL_Blog = "https://m.blog.naver.com/Recommendation.naver"

# 네이버 로그인 창 열기
driver.get(URL_NAVER)
time.sleep(2)
ID = "#id"
PW = "#pw"

# 아이디 인풋 클릭하기
ID_input = driver.find_element(By.CSS_SELECTOR, ID)
ID_input.click()
time.sleep(1)

# 근데 복사 붙여넣기로 해야지 자동방지 입력 문자가 안뜸
# 아이디 복사 (control + v)
pyperclip.copy(USER_ID)
time.sleep(1)
ID_input.send_keys(Keys.CONTROL, "v")

# 비밀번호 인풋 클릭하기
PW_inpout = driver.find_element(By.CSS_SELECTOR, PW)
PW_inpout.click()
time.sleep(1)

# 비번 복사 (control + v)
pyperclip.copy(USER_PW)
PW_inpout.send_keys(Keys.CONTROL, "v")
time.sleep(1)

login_btn = "#log\.login"
Enter = driver.find_element(By.CSS_SELECTOR, login_btn)
Enter.click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#new\\.dontsave").click()

input() #엔터를 누르면 넘어가게 함

driver.get(URL_Blog)
time.sleep(2)

link_selector = ".postlist__qxOgF > a"
# 스크롤 함수 생성
def scroll_to_bottom(driver):
    driver.execute_script("window.scrollBy(0,10000);")
    import random
    random_time = random.uniform(1,3) #랜덤함수, 1~3의 사이의 체류시간
    time.sleep(random_time)


# 백개의 링크가 나올 때 까지 스크롤하기
max_content = 50
all_link_list = []
previous_length = 0  # 이전에 수집한 링크 수

while len(all_link_list) < max_content:
    scroll_to_bottom(driver)
    time.sleep(1)

    all_element = driver.find_elements(By.CSS_SELECTOR, link_selector)
    for link_element in all_element:
        all_link_list.append(link_element.get_attribute('href')) 
    all_link_list = list(set(all_link_list))
    
    if len(all_link_list) == previous_length:
        break
    previous_length = len(all_link_list)

# 수집된 링크 출력
for link in all_link_list:
    print(link)

input()