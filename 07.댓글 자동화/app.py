import re
import time
import openai
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# 비번 암호화 필요
USER_ID = "비밀"
USER_PW = "비밀"


def 댓글_생성(블로그_글):
    openai.api_key = "비밀"

    # 프롬프트 생성
    프롬프트 = "위 글에 대한 너의 생각을 구어체를 사용해서 50글자 길이의 댓글로 작성해줘"
    contents = 블로그_글 + 프롬프트

    try:
        # API 호출
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=contents,
            max_tokens=100,  # 출력의 길이를 제한
            temperature=0.7  # 창의성 설정
        )

        result = response['choices'][0]['text'].strip()  # 생성된 댓글 반환
        return result
    except openai.error.RateLimitError:
        print("API 호출 한도를 초과했습니다. 잠시 후 다시 시도하세요.")
        
        #안되면 끝내줘
        driver.quit()




def scroll_to_bottom(driver):
    # 페이지 스크롤 다운
    driver.execute_script("window.scrollBy(0,10000);")
    time.sleep(2)  # 일정 시간 대기


# WebDriver 초기화
driver = webdriver.Chrome()

# URL 설정
URL_NAVER = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com"
URL_Blog = "https://m.blog.naver.com/Recommendation.naver"

# 네이버 로그인 창 열기
driver.get(URL_NAVER)
time.sleep(2)

# 아이디, 비밀번호 입력
ID_input = driver.find_element(By.CSS_SELECTOR, "#id")
pyperclip.copy(USER_ID)
ID_input.send_keys(Keys.CONTROL, "v")
time.sleep(1)

PW_input = driver.find_element(By.CSS_SELECTOR, "#pw")
pyperclip.copy(USER_PW)
PW_input.send_keys(Keys.CONTROL, "v")
time.sleep(1)

# 로그인 버튼 클릭
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\\.login")
login_btn.click()
time.sleep(1)

# "로그인 유지 안함" 클릭
driver.find_element(By.CSS_SELECTOR, "#new\\.dontsave").click()
time.sleep(1)

# 블로그 페이지로 이동
driver.get(URL_Blog)
time.sleep(2)

# 링크 선택자
link_selector = ".postlist__qxOgF > a"

# 원하는 링크 개수 수집
max_content = 3
all_link_list = []
previous_length = 0  # 이전에 수집한 링크 수

while len(all_link_list) < max_content:
    scroll_to_bottom(driver)
    all_element = driver.find_elements(By.CSS_SELECTOR, link_selector)
    
    for link_element in all_element:
        all_link_list.append(link_element.get_attribute('href'))
    all_link_list = list(set(all_link_list))  # 중복 제거

    if len(all_link_list) == previous_length:
        break
    previous_length = len(all_link_list)

# 수집된 링크 출력
print("수집된 링크들:")
for link in all_link_list:
    print(link)

# 블로그 글에서 댓글 생성
for link in all_link_list:
    # 정규식 표현 사용하여 블로그 ID와 로그 번호 추출
    BLOG_ID = re.search(r"https://m\.blog\.naver\.com/([^/]+)", link).group(1)
    LOG_NUM = re.search(r"https://m\.blog\.naver\.com/[^/]+/(\d+)", link).group(1)
    
    # URL 만들기
    url = f"https://m.blog.naver.com/{BLOG_ID}/{LOG_NUM}?referrerCode=1"
    
    # 해당 URL로 이동
    driver.get(url)
    time.sleep(3)

    # 블로그 글 내용 추출
    블로그_글 = driver.find_element(By.CSS_SELECTOR, ".se-main-container").text
    print("---------------")
    print("블로그 글 내용:")
    print(블로그_글)
    print("---------------")

    # 댓글 생성
    생성된_댓글 = 댓글_생성(블로그_글)

    print("---------------")
    print("생성된 댓글:")
    print(생성된_댓글)
    print("---------------")
    print("Lock")
    
    input("다음 블로그로 넘어가려면 엔터를 누르세요.")

# WebDriver 종료
# 답글 얻으면 밑에 textbar에 붙여넣고 등록 클릭하게 하면 되는거 아닌가

driver.quit()
