import requests

# 구글의 정보를 가져옴
res = requests.get('https://google.com')
# 웹페이지를 가져오는데 문제가 있으면 에러를 내 버림
res.raise_for_status()

if res.status_code == requests.codes.ok:
    print('it is OK')
    print('웹 스크래핑을 진행합니다')

# res.text -> 가져온 문서의 텍스트를 봄
with open('mygoogle.html', 'w', encoding='utf-8') as f:
    f.write(res.text)