# 동적페이지에 대한 스크래핑 작업!
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Accept-Language': 'en-US,en'
}
url = 'https://play.google.com/store/movies/top'
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs={'class': 'WHE7ib mpg5gc'})
print(len(movies))  # 이게 왜 0일까?

with open('movie.html', 'w', encoding='utf-8') as f:
    # f.write(res.text)
    f.write(soup.prettify())  # html 문서를 예쁘게 출력해줌
# 구글무비에서는 접속하는 사용자와 위치에 따라 다른 정보를 출력해주기 떄문에 내가 보는 정보와 requests로 가져오는 정보가 다르다!
# 헤더에 Accept-Language를 통해서 나의 정보를 알려주면 한국에 맞는 영화를 추천해준다

for movie in movies:
    title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()
    print(title)

# 그러나 10개밖에 없음. 이는 구글무비 페이지에서 동적으로 영화들을 10개씩 받아오기 때문