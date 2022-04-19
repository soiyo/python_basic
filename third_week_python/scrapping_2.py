# beautifulsoup 사용해보기 : 영화명 가져오기
# 라이브러리 import
import requests
from bs4 import BeautifulSoup

#라이브러리 내장 함수 사용
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#가져올 사이트 규칙 찾기
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

#movies 변수 설정
movies = soup.select('#old_content > table > tbody > tr')

#리스트 형태로 데이터를 가져오기 때문에 반복문의 형태로 한 줄씩 모두 출력하기
for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None: #None이라는 게 중간중간 뜨니까 없애주기
        print(a.text)