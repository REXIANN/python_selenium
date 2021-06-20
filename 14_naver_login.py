from selenium import webdriver
import time
path = '/Users/jinhyuck/Documents/python_selenium/chromedriver'
browser = webdriver.Chrome(path)

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. 아이디 및 패스워드 입력
browser.find_element_by_id('id').send_keys('gandolkim7')
browser.find_element_by_id('pw').send_keys('84pztn32r5')
time.sleep(1)
browser.find_element_by_id('log.login').click()
# 자동입력 방지 탭이 뜬다... ㅋㅋㅋㅋㅋ 아쒸...

browser.find_element_by_id('id').clear()  # 해당 엘리먼트에 입력한 값을 지움

print(browser.page_source)  # 브라우저가 가진 모든 소스정보를 보여준다

browser.quit()
