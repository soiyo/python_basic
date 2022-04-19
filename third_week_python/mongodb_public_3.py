#pymongo update
from pymongo import MongoClient
#//id:password ~ 클러스터이름?
client = MongoClient('클러스터 url')
db = client.people #콜렉션 (소제목)

# db.users.update_one({'name':'bob'},{'$set':{'age':19}}) #업데이트 조건 : Name이 bob, 나이를 19로 만들어라
db.users.delete_one({'name':'bob'})

#회원가입, 탈퇴할때 쓰일듯. bob을 2개 만들고 delete를 실행해보면 하나만 지워지는 것으로 보아, 왜 id 중복이 안되는지 알 수 있음.