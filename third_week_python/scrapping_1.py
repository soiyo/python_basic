# beautifulsoup 사용해보기
import requests
from bs4 import BeautifulSoup

# 브라우저에서 콜 날린것처럼 써주는거임
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 가져오고 싶은 곳의 url
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 브라우저 콘솔창에서 copy selector
# 한 줄만 가져오기
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title.text) #영화이름출력
print(title['href']) #영화이름 앞 출력

# 여러 줄 가져오기
movies = soup.select('#old_content > table > tbody > tr:nth-child(4) > td.title > div > a')
print(movies) #리스트형태로 출력됨
