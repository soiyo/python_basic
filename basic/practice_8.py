#파이썬 심화 문법

#튜플? : 리스트랑 같이 순서가 있는 자료형이지만 불변형
#리스트 사용시 뭘 넣을 수 있음
a=['사과','감','배']
a[1]='수박'
print(a)

#튜플 사용시 뭘 넣을 수 없음
b=('사과','감','배')
# b[1]='수박' > 바꿀 수 없음 : 'tuple' object does not support item assignment
print(b[1])

#튜플의 쓰임 : 주로 바뀌지 않는 정보작성에 쓰임
people_dict = [{'name':'bob', 'age' :27},{'name':'john', 'age' :30}]#리스트 안에 딕셔너리 들어감. 이 딕셔너리를 간략화해줌
people = [('bob',27),('john',30)] #people의 모든 요소에 0번째는 이름 , 1번째는 나이

#집합 : 중복을 제거해줌
c=[1,2,3,4,5,1,2,3,5,6,7]
c_set = set(c)
print(c_set)

#교집합
d=['사과','감','배','수박','딸기']
e=['배','감','포도','참외']
d_set = set(d)
e_set = set(e)
print(d_set& e_set)
#합집합
print(d_set|e_set)
#차집합
print(d_set-e_set)

#차집합 퀴즈
student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']
set_a=set(student_a)
set_b=set(student_b)
print(set_a-set_b)#a합b -b

