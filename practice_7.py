#함수
def hello():
    print("함수 기본 틀")
hello()

#두 수의 합 구하는 함수
def sum(a,b):
    return a+b
result = sum(1,2) #1이 a에, 2가 b에 들어감
print("두 수를 더하면" + str(result))

#버스요금내기
def bus_rate(age):
    if age>65:
        return "무료입니다. 내야할 금액은 "+str(0)+"원 입니다."
    elif age>20:
        return "성인입니다. 내야할 금액은 "+str(1200)+"원 입니다."
    else:
        return "어린이입니다. 내야할 금액은 "+str(750)+"원 입니다."
myrate=bus_rate(15)
print(myrate)

#주민번호 짝수이면 여자 홀수이면 남자
def check_gender(pin):
    gender = pin.split('-')[1][0]
    if int(gender)%2==0: #문자열 정수로 바꾸기
        print('여자입니다.')
    else :
        print('남자입니다.')
check_gender('150101-1012345')
check_gender('150101-2012345')
check_gender('150101-4012345')
