"""
분산 임베딩
Word2Vec
-신경망 기반 단어 임베딩
- CBOW, skip-gram
-Gensim 패키지 사용
"""
from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

#네이버 영화 리뷰 데이터 읽어옴
# def read_review_data(filename):
#     with open(filename, 'r',encoding='UTF-8') as f:
#         data = [line.split('\t') for line in f.read().splitlines()]
#         data = data[1:] # header 제거
#     return data
#
#
# # 측정 시작
# start = time.time()
#
# # 리뷰 파일 읽어오기
# print('1) 말뭉치 데이터 읽기 시작')
# review_data = read_review_data('./ratings.txt')
# print(len(review_data)) # 리뷰 데이터 전체 개수
# print('1) 말뭉치 데이터 읽기 완료: ', time.time() - start)
#
# # 문장단위로 명사만 추출해 학습 입력 데이터로 만듬
# print('2) 형태소에서 명사만 추출 시작')
# komoran = Komoran()
# docs = [komoran.nouns(sentence[1]) for sentence in review_data]
# print('2) 형태소에서 명사만 추출 완료: ', time.time() - start)
#
# # word2vec 모델 학습
# print('3) word2vec 모델 학습 시작')
# model = Word2Vec(sentences=docs, size=200, window=4, min_count=2, sg=1)
# print('3) word2vec 모델 학습 완료: ', time.time() - start)
#
# # 모델 저장
# print('4) 학습된 모델 저장 시작')
# model.save('nvmc.model')
# print('4) 학습된 모델 저장 완료: ', time.time() - start)
#
# # 학습된 말뭉치 개수, 코퍼스 내 전체 단어 개수
# print("corpus_count : ", model.corpus_count)
# print("corpus_total_words : ", model.corpus_total_words)
#



# 학습된 모델 불러오기
# 모델 로딩
model = Word2Vec.load('nvmc.model')
print("corpus_total_words : ", model.corpus_total_words)

# '사랑'이란 단어로 생성한 단어 임베딩 벡터
print('사랑 : ', model.wv['사랑'])

# 단어 유사도 계산
print("일요일 = 월요일\t", model.wv.similarity(w1='일요일', w2='월요일'))
print("안성기 = 배우\t", model.wv.similarity(w1='안성기', w2='배우'))
print("대기업 = 삼성\t", model.wv.similarity(w1='대기업', w2='삼성'))
print("일요일 != 삼성\t", model.wv.similarity(w1='일요일', w2='삼성'))
print("히어로 != 삼성\t", model.wv.similarity(w1='히어로', w2='삼성'))

# 가장 유사한 단어 추출
print(model.wv.most_similar("안성기", topn=5))
print(model.wv.most_similar("시리즈", topn=5))
##
