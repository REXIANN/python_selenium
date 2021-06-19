# requests로 웹사이트 접속시 403 에러가 뜨는 경우가 있음
# 우리가 사이트에 접속을 할 때 웹사이트도 우리를 알아본다
# http://nadocoding.tistory.com의 경우 requests로 들어가면 에러가 난다. 이부분을 유저에이전트로 해결 가능
# whatismybrowser.com 에서 나의 user agnet를 확인할 수 있다.

import requests

url = 'http://nadocoding.tistory.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open('nadocoding.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

