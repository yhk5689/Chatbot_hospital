from konlpy.tag import Komoran
"""
morphs() : 형태소 단위로 토크나이징. 토크나이징된 형태소들은 리스트 형태로
nouns() : 품사가 명사인 토큰들만 추출
pos( , flatten=True) : 입력한 문장에서 형태소를 추출한 뒤 품사태깅
- 추출된 형태소와 그 형태소의 품사가 튜플 형태로 묶여서 리스트로 반환됨
NNG : 일반명사
JKS : 주격 조사
JKB : 부사격 조사
VV : 동사
EF : 종결 어미
SF : 마침표
[참고] : http://docs.komoran.kr/firststep/postypes.html
"""
def get_keywords(pos, without_tag = False) :
    exclusion_tags = [          # 예외처리할 품사
        'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
        'JX', 'JC',
        'SF', 'SP', 'SS', 'SE', 'SO',
        'EP', 'EF', 'EC', 'ETN', 'ETM',
        'XSN', 'XSV', 'XSA'
    ]
    f = lambda x: x in exclusion_tags
    word_list = []
    for p in pos:
        if f(p[1]) is False:
            word_list.append(p if without_tag is False else p[0])
    return word_list
# 코모란 형태소 분석기 객체 생성
# komoran = Komoran()
# text = "성남에 있는 성심병원의 주소를 알려주세요."
#
# # 형태소 추출
# morphs = komoran.morphs(text)
# print(morphs)
#
# # 형태소와 품사 태그 추출
# pos = komoran.pos(text)
# print(pos)

# 명사만 추출
# nouns = komoran.nouns(text)
# print(nouns)

#인식이 안되는 새로운 단어 추가
#[단어] TAP [품사]
#엔엘피 NNG
komoran = Komoran(userdic='./user_dic.txt') # 사용자사전 1 병원이름 정의 X
komoran2 = Komoran(userdic='./user_dic_2.txt')  # 사용자사전 2 병원이름 정의 O
text = "용인에 있는 한성의심원병원 전화번호 알려줘!"
pos = komoran.pos(text)
pos2 = komoran2.pos(text)
print(pos)
print(pos2)
# print(get_keywords(pos, without_tag=False))
# print(get_keywords(pos, without_tag=True))


