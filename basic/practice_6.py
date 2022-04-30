#6_연습문제

#리스트에서 짝수만 출력하는 함수 만들기
num_list = [1,2,3,6,3,2,4,5,6,2,4]
for num in num_list:
    if num%2==0:
        print(num) #궁금한점:한줄에 붙여서 출력하는 방법은?
        
#리스트에서 짝수 개수 출력
count=0
for num in num_list:
    if num%2==0:
        count+=1 #count=count+1
print('리스트에서 짝수 개수 : '+str(count))
        
#리스트에서 안에 있는 모든 숫자 더하기
sum=0
for num in num_list:
    sum+=num #sum=sum+num
print('모든 숫자를 합한 값 : '+str(sum))

#리스트 안에 있는 자연수 중 가장 큰 숫자 구하기 <- 이 문제 못품
max=0
for num in num_list:
    if max<num:
        max=num
        
print('리스트 안에 있는 수 중 가장 큰 숫자는 : '+str(max))
print(max(num_list))

#시도해본것 (마지막문제)
# for i, num in enumerate(num_list):
     
        
    # if num>num[i]:
    #     print(num)
    # else:
    #     print(num+1)

#이건 뭘까?
# print('--')
# for i in num_list:
#     num=num_list[i]
#     print(num)