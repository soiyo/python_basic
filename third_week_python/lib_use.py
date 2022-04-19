# requests 라이브러리 사용해보기_기본

import requests # requests 라이브러리 설치 필요

#라이브러리 내장 함수 사용
r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row'] #가져올 곳 변수
for row in rows:
    gu_name = row['MSRSTE_NM'] #가져올값
    gu_mise = row['IDEX_MVL']
    if gu_mise <60: #미세먼지 농도 60이하 값만 출력
        print(gu_name,gu_mise) #서울의 지역, 미세먼지 정도 출력