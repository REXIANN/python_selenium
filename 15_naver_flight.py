from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path = '/Users/jinhyuck/Documents/python_selenium/chromedriver'
browser = webdriver.Chrome(path)

# 1. 네이버로 이동
browser.get("http://naver.com")
browser.maximize_window()  # 창 최대화. 정확하게 모니터 사이즈로는 커지지 않는다?!

url = 'https://flight.naver.com/flights/'
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text('가는날 선택').click()

# 이번달 27일, 다음달 28일 선택
# 27을 가지는 모든 엘리먼트를 가져와서 첫번째를 선택(이번 달)
browser.find_elements_by_link_text('27')[0].click()  # [0] -> 이번달
browser.find_elements_by_link_text('28')[1].click()  # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()
# 굳이 최하위 경로를 찾아서 클릭할 필요 없음!

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 첫번째 결과 출력 - 실패 케이스
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)  # no such element 라고 나온다. 로딩을 기다리지 않았기 때문!

# time.sleep()으로 몇초동안 기다리도록 설정할 수 있으나 이는 비효율적임
# 대신 해당 엘리먼트가 등장할때까지 기다리도록 할 수 있음!

# 첫번째 결과 출력
# browser에 대해 어떠한 엘리먼트가 위치할 떄 까지 10초동안 기다림
# EC: 기대하고 있는 조건
# By: ~의 조건
try:  # 에러가 날 경우 그냥 하위작업 수행할 필요 없이 finally로 직행
    elem = WebDriverWait(browser, 10)\
        .until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    time.sleep(2)
    print(elem.text)  # 첫번쨰 li가 가진 text정보들을 출력

finally:
    # 브라우저 종료
    browser.quit()
