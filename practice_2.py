#2_문자열: 따옴표가 붙어야 문자열
import re

#문자열 변수 지정 : 따옴표 이용하면 됨
first_name = 'hyeon'
last_name = ' yun'
age = 100 #얘는 문자열 아님
#2를 문자열로 지정하는 방법 2번째 : str()이용
char = str(2) #문자열2와 숫자2는 다름
print(first_name+last_name)

#문자열 first_name, last_name 두개는 그냥 합쳐짐
print(first_name+last_name+" age is "+str(age))

#문자열 자르기
print(len(first_name)) #문자열 길이세기
print(first_name[:3]) #앞으로부터 3개까지 잘라라
print(first_name[3:]) #앞으로부터 4번째부터 출력 (인덱스 0부터시작)
print(first_name[3:4]) #앞으로부터 4번째~4번째까지 출력
print(first_name[:]) #텍스트 그대로 출력 

#문자열 자르기 실습
sparta = 'sparta'
result = sparta
print(result[:3])

#문자열 자르기 실습2
email = 'hello@gmail.com' #문자열 자르기 : split 시 리스트형태로 출력, 인덱스로 꺼내기
print(email.split('@'))
print(email.split('@')[1])
print(email.split('@')[1].split('.'))
print(email.split('@')[1].split('.')[1])

#문자열 자르기 실습 3
phone = '010-1234-1234'
result_phone = phone.split('-')[0]
print(result_phone)

