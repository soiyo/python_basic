#f-string

#OO의 점수는 OO입니다.
scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}    
] #리스트 안 딕셔너리 여러개 있을 때
for s in scores:
    name = s['name']
    score = s['score']
    # print(name+"의 점수는 "+str(score)+"점 입니다.")
    print(f'{name}의 점수는 {score}점 입니다.') #f-string : 문자열 표현식이 간단해짐
    