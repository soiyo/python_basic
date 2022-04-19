# pymongo 사용해보기_게시용
from pymongo import MongoClient
#//id:password ~ 클러스터이름?
client = MongoClient('클러스터 url')
db = client.people #콜렉션 (소제목)

# 데이터 집어넣기 > Database > Browse > collection에 아래 데이터 들어가있는 것을 볼 수 있음
doc = {
    'name':'bob',
    'age':27
}
#users(콜렉션제목) 콜렉션에 넣음
db.users.insert_one(doc)