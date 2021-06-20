from selenium import webdriver

# 크롬 웹 드라이버 객체를 생성함
# 만일 다른 경로에 있는 chromedriver를 가져온다면 Chrome()의 괄호 안에 경로 적어줘야함
path = '/Users/jinhyuck/Documents/python_selenium/chromedriver'
browser = webdriver.Chrome(path)

browser.get("http://naver.com")

# 이제 터미널에 python 명령어를 통해 브라우저를 띄워서 진행함

elem = browser.find_element_by_class_name('link_login')
# elem을 찍어보면 selenium.WebElement로 선택된 것을 볼 수 있다

# 로그인 버튼 클릭
elem.click()

browser.back()  # 뒤로가기
browser.forward()  # 앞으로가기
browser.refresh()  # 새로가기

# 검색창 가져오기
elem = browser.find_element_by_id('query')

from selenium.webdriver.common.keys import Keys # 이걸 가져옴으로써 키입력을 할 수 있다
elem.send_keys('나도 코딩')  # 입력창에 입력
elem.send_keys(Keys.ENTER)  # 엔터키 입력. 실제로 import한 Keys가 사용되는 부분

# 여러 개의 엘리먼트를 가져오고 싶으면 find_뒤에 s를 붙이자!
elem = browser.find_elements_by_tag_name('a')

for e in elem:
    # 속성값을 전부 가져옴
    e.get_attribute('href')

# 다른 페이지로 이동
browser.get('http://daum.net')

elem = browser.find_element_by_name('q')
elem.send_keys('ss')
elem_click = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')

# 브라우저 종료
browser.close()  # 현재 열려있는 브라우저 탭 종료
browser.quit()  # 브라우저 자체를 종료