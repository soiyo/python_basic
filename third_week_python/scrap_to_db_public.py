# beautifulsoup 하고 pymongo 엮기
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('클러스터 url')
db = client.people

#라이브러리 내장 함수 사용
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#movies 변수 설정 : tr까지는 가져옴(가져올 데이터들의 공통분모)
movies = soup.select('#old_content > table > tbody > tr') 
for movie in movies: #모든 값 쭉 가져오고
    a=movie.select_one('td.title > div > a')# 리스트 형태로 title 데이터를 가져오기 때문에 반복문의 형태로 한 줄씩 모두 출력하기
    if a is not None: #title 의 None값 제거
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']#alt값만 뽑아오기
        star = movie.select_one('td.point').text#별점가져오기
        doc={#db에 저장
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)