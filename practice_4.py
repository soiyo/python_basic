#4_조건문은 if와 else만 알면 됨
money = 3000
if money >3800: #money>3800이면
    print('택시를 타자') #여기 실행
elif money >1200:
    print('버스를 타자')
else:
    print('택시를 못타') #money<=3800이면 여기 실행
    print('그럼 뭘 타지?')
    print('그냥 걸어가자!')

