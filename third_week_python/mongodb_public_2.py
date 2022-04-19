# pymongo 사용해보기_게시용
from pymongo import MongoClient
#//id:password ~ 클러스터이름?
client = MongoClient('클러스터 url')
db = client.people #콜렉션 (소제목)

# 데이터 모두 보기
all_users = list(db.users.find({},{'_id':False})) #find{조건}, 리스트보기
for user in all_users:
    print(user)

# 하나만 보기
user = db.users.find_one({'name':'bob'})
print(user)
print(user['age'])#bob의 age만 보기