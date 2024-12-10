from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pyperclip
import time

driver = webdriver.Chrome()

# URL 정리 (강의에서는 이렇게 안했는데, 난 이게 더 보기 좋다)
URL_NAVER = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com"
URL_Blog = "https://m.blog.naver.com/Recommendation.naver"


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
import re 
for link in all_link_list:
    # 정규식 표현 사용하여 내용 뽑아오기
    BLOG_ID = re.search(r"https://m\.blog\.naver\.com/([^/]+)", link).group(1)
    LOG_NUM = re.search(r"https://m\.blog\.naver\.com/[^/]+/(\d+)", link).group(1)
    url = f"https://m.blog.naver.com/{BLOG_ID}/{LOG_NUM}?referrerCode=1"
    driver.get(url)
    time.sleep(3)

    블로그_글 = driver.find_element(By.CSS_SELECTOR, ".se-main-container")
    블로그_글 = 블로그_글.text
    print(블로그_글)
