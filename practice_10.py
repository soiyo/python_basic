#예외처리
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]
# for person in people:
#     if person['age']>20: #20살보다 많은 사람
#         print(person['name']) #이름찍어주기

#근데 만약 bobby의 age가 없다면?
for person in people:
    try:#얘를 실행시키다가
        if person['age']>20: #20살보다 많은 사람
            print(person['name']) #이름찍어주기
    except:#에러가 나면 얘를 실행할것
        print(person['name'],'에러입니다') #어디에서 에러 났는지 확인 가능
        
# 이 기능 : 서버에서 잘못되었을경우가 있을때 try-except문으로 잡아주면 큰 무리없이 돌아가기 가능
# 근데 남용하면 돌아가는데 무슨 에러 났는지 모르게되니 웬만하면 안 사용할것
