import requests
import xmltodict
import json
"""
SIGUN_CD	시군코드
SIGUN_NM	시군명
BIZPLC_NM	사업장명
REFINE_ROADNM_ADDR	소재지도로명주소
REFINE_LOTNO_ADDR	소재지지번주소
REFINE_ZIP_CD	소재지우편번호
BSN_STATE_NM	영업상태명
LOCPLC_FACLT_TELNO	소재지시설전화번호
MEDINST_ASORTMT_NM	의료기관종별명
MEDSTAF_CNT	의료인수
HOSPTLRM_CNT	입원실수
SICKBD_CNT	병상수
TREAT_SBJECT_CONT_INFO	진료과목내용정보
REFINE_WGS84_LAT	위도
REFINE_WGS84_LOGT	경도

의도
인사 - 0 
정보제공 - 1
병원전체 정보제공 - 1-1
        진료과목 - 1-2
        주소 - 1-3
        전화번호 - 1-4
        
병원 리스트 제공 - 2 
    지역(시) 병원 리스트 - 2-1
    지역(시) + 지역(동) 병원리스트 - 2-2
    지역(시) + 의료기관종 병원리스트 - 2-3
    지역(시) + 진료과목 병원리스트 - 2-4
    
# 길찾기, 기타등등
"""
def remove_redundancy(list_A) :           # list 중복제거 함수
    set_list = set(list_A)
    remove_list = list(set_list)
    return remove_list

# 파일경로 지정
# corpus.txt에 총 학습 data 저장
f = open('test_corpus.txt', 'a',encoding= 'utf-8')
# f = open('../utils/user_dic.txt', 'a', encoding= 'utf-8')

"""
*   아래 url 2개 다 사용해야 합니다. (모든 data)
*   사용할 부분만 주석 풀어서 사용하시면 됩니다.
*   주석제거 tip) - 드래그 한뒤 Ctrl + / (안될시 한/영키 확인)
*   띄어쓰기 주의! File에 write후 확인 
*   f.wirte 부분만 계속 바꿔가면서 write 하면 됨.
*   write하기전에 print해서 한번 확인해볼 것.
"""
url = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pSize=1000"
url2 = "https://openapi.gg.go.kr/GgHosptlM?KEY=337b4bebd30e4d419b85a1ba8c9c26a2&pIndex=2&pSize=1000"
content = requests.get(url).content
content2 = requests.get(url2).content

dict = xmltodict.parse(content)
dict2 = xmltodict.parse(content2)

jsonString = json.dumps(dict['GgHosptlM']['row'], ensure_ascii=False)   # <GgHosptlM> 태그의 <row> 정보
jsonString2 = json.dumps(dict2['GgHosptlM']['row'], ensure_ascii=False)

jsonObj = json.loads(jsonString)
jsonObj2 = json.loads(jsonString2)



# Intent 1
# for tag in jsonObj :
#     if tag['BSN_STATE_NM'] == '영업중' :
#           print('0000' + '\t' + tag['BIZPLC_NM'] + ' 병원' + '\t\t' + '1' + '\n')
#           f.write('0000' + '\t' + tag['BIZPLC_NM'] + ' 병원' + '\t\t' + '1' + '\n')    # 띄어쓰기 주의 intent 1에 속하면 1, 2에 속하면 2



# Intent 2-1
# sigun = []
# for item in jsonObj :
#     if item['BSN_STATE_NM'] == '영업중' :
#        sigun.append(item['SIGUN_NM'])
# sigun = remove_redundancy(sigun)
#
# for i in sigun :
#     print('0000' + '\t' + i + ' 병원목록' + '\t\t' + '2' + '\n')
#     f.write('0000' + '\t' + i + ' 병원목록' + '\t\t' + '2' + '\n')


# Intent 2-2
# adress = []
# union = []
# new_union = []
# for tag in jsonObj :
#     if tag['BSN_STATE_NM'] == '영업중' :
#         add = str(tag['REFINE_LOTNO_ADDR']).split(' ')
#         if len(add) >= 3 :
#             adress.append(add[1:3])
#
# for tag2 in jsonObj2 :
#     if tag2['BSN_STATE_NM'] == '영업중' :
#         add2 = str(tag2['REFINE_LOTNO_ADDR']).split(' ')
#         if len(add2) >= 3 :
#             adress.append(add2[1:3])
#
# for i in adress :
#         if i not in union :
#             union.append(i)
# for i in union :
#     new_union.append(i[0] + ' ' + i[1])
#
# for i in new_union :
#     print('0000' + '\t' + i + ' 병원 목록' + '\t\t' + '2' + '\n')
    # f.write('0000' + '\t' + i + ' 병원 목록' + '\t\t' + '2' + '\n')


#   Intent 2-3
# sigun = []; subject = []
# for item in jsonObj :
#     if item['BSN_STATE_NM'] == '영업중' :
#        sigun.append(item['SIGUN_NM'])
#        subject.append(str(item['MEDINST_ASORTMT_NM'])[0:4])
# sigun = remove_redundancy(sigun); subject = remove_redundancy(subject)
#
# for i in sigun :
#     for j in subject :
#         print('0000' + '\t' + i + ' ' + j + ' 목록' +
#                 '\t\t' + '2' + '\n')    # i = 시 j = 병원 (종)

#         f.write('0000' + '\t' + i + ' ' + j + ' 목록' +
#                 '\t\t' + '2' + '\n')    # i = 시 j = 병원 (종)


#   Intent 2-4
# sigun = []; treat = []
# for tag in jsonObj :
#     if tag['BSN_STATE_NM'] == '영업중' :
#         sigun.append(tag['SIGUN_NM'])
#
#         treat_split = str(tag['TREAT_SBJECT_CONT_INFO']).split(', ')
#         for i in treat_split :
#             treat.append(i)
#
# for tag2 in jsonObj2 :
#     if tag2['BSN_STATE_NM'] == '영업중':
#         treat_split2 = str(tag2['TREAT_SBJECT_CONT_INFO']).split(', ')
#         for i in treat_split2 :
#             treat.append(i)
# sigun = remove_redundancy(sigun); treat = remove_redundancy(treat)
#
# for i in sigun :
#     for j in treat :
#         print('0000' + '\t' + i + ' ' + j + ' 병원' +
#                 '\t\t' + '2' + '\n')    # i = 시 j = 병원 (진료과목)

#         f.write('0000' + '\t' + i + ' ' + j + ' 병원' +
#                 '\t\t' + '2' + '\n')    # i = 시 j = 병원 (진료과목)

f.close












# 배제
# url2 = "https://openapi.gg.go.kr/ChildNightTreatHosptl?KEY=77cb354acba545899e78bf1bfe9c159c&pSize=1000"
# content2 = requests.get(url2).content
# dict2 = xmltodict.parse(content2)
# jsonString2 = json.dumps(dict2['ChildNightTreatHosptl']['row'], ensure_ascii=False)
# jsonObj2 = json.loads(jsonString2)

