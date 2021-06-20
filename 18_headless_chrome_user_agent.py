""" headless모드를 사용할 때 주의할 점 """
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
# options에 user-agent를 추가해줌
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')

path = '/Users/jinhyuck/Documents/python_selenium/chromedriver'
browser = webdriver.Chrome(path, options=options)

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
"""
print를 찍어보면 본인이 HeadlessChrome임을 밝히고 있다.
따라서 몇몇 사이트는 Headless의 경우 접근을 거부하도록 설정할 수 있다
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
AppleWebKit/537.36 (KHTML, like Gecko)
HeadlessChrome/91.0.4472.114 Safari/537.36
"""

browser.quit()
