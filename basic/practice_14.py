#함수의 매개변수 다루기 (라이브러리에서 자주 출몰)

def cal(a,b):
    return a+2*b
result = cal(1,2)
# result = cal(b=2, a=1) 도 가능
print(result)


def cal(a,b=2):
    return a+2*b
result = cal(1) #안넣으면 b는 고정값으로 출력
print(result)

def cal(*args): #무한개의 인자 받기
    for name in args:
        print(f'{name} time to lunch')
cal('person1','person2')

def cal(**kwargs): #키워드 인수를 받기, 딕셔너리로 출력됨
    print(kwargs)
cal(name='bob', age=30, height=180)#딕셔너리 쓸수있게 만듬