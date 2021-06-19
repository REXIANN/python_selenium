from bs4 import BeautifulSoup
import requests

# 네이버 웹툰의 정보 가져오기
url = 'https://comic.naver.com/webtoon/weekday.nhn'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
res = requests.get(url)
res.raise_for_status()  # 혹시 문제가 있으면 바로 종료

soup = BeautifulSoup(res.text, 'lxml')
print(soup.title)  # 타이틀을 반환
print(soup.title.get_text())  # 타이틀 안의 텍스트만 반환
print(soup.a)  # soup 객체에서 첫번쨰로 발견한 a 엘리먼트를 반환
print(soup.a.attrs)  # a 태그가 가지고 있는 속성들을 볼 수 있음
print(soup.a['href'])  # a 태그가 가진 속성 중 하나만 가져옴

# 해당 클래스를 가지는 첫번째 엘리먼트를 가져옴. find에 태그 입력 안해도 가능함!
print(soup.find('a', attrs={'class': 'Nbtn_upload'}))

rank1 = soup.find('li', attrs={'class': 'rank01'})
print(rank1.a.get_text())

# 찾은 태그에서 다음 태그 또는 이전태그로 넘어갈 수도 있음
# next_sibling, previous_sibling
print(rank1.next_sibling)  # 이거는 안나옴
print(rank1.next_sibling.next_sibling)  # 이거는 나옴 -> 개행문자가 있어서 그럴 수도 있음
rank2 = rank1.next_sibling.next_sibling
# 사실 더 간단하게 다음꺼 찾을 수 있음...
rank1.find_next_sibling('li')  # 기준태그에서 다음 li를 만날 때 까지 진행

# 찾은 태그에서 부모 태그로 넘어갈 수도 있음
parent_rank = rank1.parent

# 형제들을 전부 가져오는 것도 가능함
print(rank1.find_next_siblings('li'))

webtoon = soup.find('a', text='열렙전사')
print(webtoon)