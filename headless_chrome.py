# 동적페이지에 대한 스크래핑 작업!
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

path = '/Users/jinhyuck/Documents/python_selenium/chromedriver'
browser = webdriver.Chrome(path, options=options)

url = 'https://play.google.com/store/movies/top'
browser.get(url)

# 기다리는 간격 설정
interval = 2
# 문서의 현재 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')
# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 로딩 대기
    sleep(interval)

    # 현재 높이를 가져와서 저장
    current_height = browser.execute_script('return document.body.scrollHeight')

    if current_height == prev_height:
        break

    prev_height = current_height

print('스크롤 완료')

# 스크롤 완료했을 때 스크린샷 찍을 수 있음
browser.get_screenshot_as_file('google_movie.png')

from bs4 import BeautifulSoup

# 밑으로 끝까지 스크롤한 브라우저의 정보를 가져옴
soup = BeautifulSoup(browser.page_source, 'lxml')

# 리스트를 사용하여 or 연산을 가능하게 할 수 있다
# movies = soup.find_all('div', attrs={'class': ['ImZGtf mpg5gc', 'Vpfmgd']})
movies = soup.find_all('div', attrs={'class': ['Vpfmgd']})
print(len(movies))

for movie in movies:
    title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()
    # print(title)

    original_price = movie.find('span', attrs={'class': 'SUZt4c djCuy'})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, '할인되지 않은 영화 제외')
        continue

    # 할인된 가격
    price = movie.find('span', attrs={'class': 'VfPpfd ZdBevf i5DZme'}).get_text()

    # 영화 링크
    link = movie.find('a', attrs={'class': 'JC71ub'})['href']
    # 올바른 링크: http://play.google.com + link
    print(f'제목: {title}')
    print(f'할인 전 금액: {original_price}')
    print(f'할인된 금액: {price}')
    print('링크: ', 'https://play.google.com' + link)
    print('-' * 80)


browser.quit()
