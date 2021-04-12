"""
n-gram 유사도
ex) 2-gram
* n을 크게 잡을수록 비교 문장의 토큰과 비교할때 카운트를 놓칠 확률이 커짐
* n을 작게 잡을수록 카운트 확률은 높아지지만 문맥파악 정확도가 떨어짐
"""

from konlpy.tag import Komoran
import numpy as np
from numpy import dot
from numpy.linalg import norm


#
# # 어절 단위 n-gram
# def word_ngram(bow, num_gram):
#     text = tuple(bow)
#     ngrams = [text[x:x + num_gram] for x in range(0, len(text))]
#     return tuple(ngrams)
#
#
# # 음절 n-gram 분석
# def phoneme_ngram(bow, num_gram):
#     sentence = ' '.join(bow)
#     text = tuple(sentence)
#     slen = len(text)
#     ngrams = [text[x:x + num_gram] for x in range(0, slen)]
#     return ngrams
#
#
# # 유사도 계산
# def similarity(doc1, doc2):
#     cnt = 0
#     for token in doc1:
#         if token in doc2:
#             cnt = cnt + 1
#
#     return cnt/len(doc1)
#
#
# sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학하였다'
# sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학하였다'
# sentence3 = '나는 맛잇는 밥을 뉴턴 선생님과 함께 먹었습니다.'



# komoran = Komoran(userdic='./user_dic.txt') # 사용자 사전 추가
# bow1 = komoran.nouns(sentence1)
# bow2 = komoran.nouns(sentence2)
# bow3 = komoran.nouns(sentence3)
#
# doc1 = word_ngram(bow1, 2)
# doc2 = word_ngram(bow2, 2)
# doc3 = word_ngram(bow3, 2)
#
# print(doc1)
# print(doc2)
# print(doc3)
#
# r1 = similarity(doc1, doc2)
# r2 = similarity(doc3, doc1)
# print(r1)
# print(r2)
"""
코사인 유사도
백터간 각도를 이용해 유사성 파악
코사인 각도를 이용함.
ngram의 경우 동일한 단어가 자주 등장하면 안좋음.
그러므로 코사인 유사도 자주 사용
"""
# 코사인 유사도 계산
def cos_sim(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))


# TDM 만들기
def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}

    for word in word_dics:
        freq_mat[word] = 0

    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1

    return freq_mat


# 단어 벡터 만들기
def make_vector(tdm):
    vec = []
    for key in tdm:
        vec.append(tdm[key])
    return vec


# 문장 정의
sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학하였다'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학하였다'
sentence3 = '나는 맛잇는 밥을 뉴턴 선생님과 함께 먹었습니다.'

# 헝태소분석기를 이용해 단어 묶음 리스트 생성
komoran = Komoran()
bow1 = komoran.nouns(sentence1)
bow2 = komoran.nouns(sentence2)
bow3 = komoran.nouns(sentence3)

# 단어 묶음 리스트를 하나로 합침
bow = bow1 + bow2 + bow3
print("bow : ", bow)
# 단어 묶음에서 중복제거해 단어 사전 구축
word_dics = []
for token in bow:
    if token not in word_dics:
        word_dics.append(token)


# 문장 별 단어 문서 행렬 계산
freq_list1 = make_term_doc_mat(bow1, word_dics)
freq_list2 = make_term_doc_mat(bow2, word_dics)
freq_list3 = make_term_doc_mat(bow3, word_dics)
print(freq_list1)
print(freq_list2)
print(freq_list3)


# 코사인 유사도 계산
doc1 = np.array(make_vector(freq_list1))
doc2 = np.array(make_vector(freq_list2))
doc3 = np.array(make_vector(freq_list3))

r1 = cos_sim(doc1, doc2)
r2 = cos_sim(doc3, doc1)
print(r1)
print(r2)

