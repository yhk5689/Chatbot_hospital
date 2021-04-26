import requests
import xmltodict
import json


f = open('api_test.txt', 'a',encoding= 'utf-8') # 학습데이터 만들기 위해..



url = "https://openapi.gg.go.kr/ API_NAME ?KEY=발급받은 KEY & Page 등 기타명령어 경기데이터드림 홈페이지 참조"
content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['GgHosptlM']['row'], ensure_ascii=False)   # <'GgHosptlm > < row > - API tag 참조
jsonObj = json.loads(jsonString)


for item in jsonObj :
    #   print(item.keys())
    if item['BSN_STATE_NM'] == '영업중' :
        print(item['BIZPLC_NM'])





