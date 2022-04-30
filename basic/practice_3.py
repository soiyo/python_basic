#3_리스트와 딕셔너리 : 값을 담는 방법에 대한 이야기
#리스트 : 순서가 중요하게 값을 담음 (0번째는 ~, 1번째는~), 타고 타고 들어가는 성질
#딕셔너리 : 키-value로 값을 담음 (주민등록번호는 ~, 생일은~)
from ast import DictComp

#리스트에 포함할 수 있는것은?
f = ['사과','배',False,['감','포도']] # 참, 거짓, 리스트를 리스트에 포함 가능.
#리스트 출력
print(f[2],f[3][1]) 
#리스트에 값 추가
f.append(00)
f.append(90)
print(f)

#리스트 자르기
cut=f[3] #4번째 값을 가지고 온다
cut_2=f[-1] #맨뒤에꺼 하나
#리스트 길이 구하기
len_1=len(f) 
print(cut,cut_2,len_1)

#리스트 내림차순 정렬
list = [1,2,3,4,5,6,7]
list.sort(reverse=True) #내림차순 정렬
print(list)

#리스트 안에 찾는 값 있는지 확인
result=5 in list #내가 원하는값 여기 있는지 없는지 알 수 있음, 5가 list에 있나?
print(result)

#딕셔너리
dict = {'name':'hyeon', 'age':'100', 'friend':['영','이']} #키와 값이 들어있음. 순서가 없음,리스트와 조합되기도 함
#딕셔너리 출력
print(dict['name'], dict['friend'][1]) #dict라는 딕셔너리의 name값을 출력해보자 (딕셔너리의 특정 값 가져옴)

#딕셔너리에 값 추가
dict['height']=180 #dict 값 추가 (값 넣기)
print(dict) 

#딕셔너리 안에 찾는 값 있는지 확인
result = 'weight' in dict #이 값이 있나요?
print(result)

#리스트, 딕셔너리 혼합 및 값 가져오기
people=[{'name':'hy', 'age':50},
        {'name':'gh', 'age':30}] #리스트 안 딕셔너리
print(people[1]['age']) #값 가져오기

#딕셔너리 퀴즈
peoples = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]
#smith의 science 점수 출력하기
print(peoples[2]['score'])
print(peoples[2]['score']['science'])

