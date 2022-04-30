#5_반복문

#반복문의 아주 기초적인 구조 (리스트 안 요소를 하나씩 꺼내서 써먹음)
#이름지어진 변수 fruit에 넣어서 씀
fruits = ['사과','배','감','수박','딸기']
for fruit in fruits:
    print(fruit)
    
#나이 출력하기
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

#원초적인 출력
print(people[0])

#사람들 다 출력
for person in people:
    print(person)
    
#person은 딕셔너리, name과 age에 해당하는 키값 가져옴 (모두)
for person in people:
    name=person['name']
    age=person['age']
    print(name, age)
    
#조건에 맞는것만 출력
print('여기서부터 조건에 맞는것만 출력')
for person in people:
    name=person['name']
    age=person['age']
    if age>20:
        print(name, age)

#조금 더 나아가서 :1000줄짜리 코딩할때 출력해보지 않아도 원하는 코딩 디버깅 가능 > 어떻게 할 수 있으려나?
print('조금 더 나아가서')
for i, person in enumerate(people): #요소의 순서를 i에 적어줌
    name=person['name']
    age=person['age']
    print(i, name, age)
    if i>3: #4까지 출력완료한 상태에서
        break
        