# 정규식 - 말 그대로 규정된 표현
import re

# 1. p = re.compile('원하는 정규식 형태')
# 2. m = p.match('비교할 문자열') 또는 p.search('비교할 문자열') 또는 p.findall('비교할 문자열')

# .: 하나의 문자를 의미 (ca.e) > care, cafe, case | caffe
# ^: 문자열의 시작 (^de) > desk, destination | fade
# $: 문자열의 끝 (se$) > case, base, source | face

# compile 은 정규화할 문장을 정의
p = re.compile('ca.e')

# match: 주어진 문자열의 처음부터 일치하는지 확인
m = p.match('case')
m = p.match('careless')  # gocare는 에러가 난다.

print(m.group())  # 일치하는 문자열 반환. 매치되지 않으면 에러가 발생
print(m.string)  # 입력받은 문자열을 그대로 표시
print(m.start())  # 일치하는 문자열의 시작 인덱스
print(m.end())  # 일치하는 문자열의 끝 인덱스
print(m.span())  # 일치하는 문자열의 시작과 끝 인덱스(튜플 형태)

# search: 주어진 문자열 중에 일치하는게 있는지 확인
s = p.search('careless')

# findall: 일치하는 모든 것을 리스트 형태로 반환
lst = p.findall('good care cafe')  # ['care', 'cafe']

# 파이썬 공식문서 또는 w3schools의 python RegEx에 들어가면 더 공부를 할 수 있다

# 앞으로 사용할 함수라 미리 만들어둠
def print_match(match):
    if match:
        print(match.group())
    else:
        print('매칭되지 않음')
