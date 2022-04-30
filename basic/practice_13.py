# 리스트 조작 연습 (map, filter, lamda 식)


people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

#함수식
# def check_adult(person):
    # if person['age']>20:
    #     return '성인'
    # else:
    #     return '청소년'
    
    #조건문 한줄식
    # return '성인' if person['age']>20 else '청소년'

#map    
# result = map(check_adult, people) #people 돌면서 check_adult함수에 넣고 리턴값 모아줘라
#map을 리스트로 출력
# print(list(result))

#람다식 map(lambda x:y, people)y를 x에 넣는다
# result = map(lambda person: ('성인' if person['age']>20 else '청소년'), people) #people 돌면서 person에 넣고 그 person을 리턴해라

#필터
result = filter(lambda person: person['age']>20, people) #20보다 큰 애들 뽑아내기

#관용적으로 이렇게 많이 쓰임
result = filter(lambda x: x['age']>20, people) #20보다 큰 애들 뽑아내기
print(list(result))
