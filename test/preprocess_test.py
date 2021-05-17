from utils.Preprocess import Preprocess

sent = "김포시에 있는 고려병원 위치 알려줘"

p = Preprocess(userdic='../utils/user_dic.txt') # 사용자 사전

pos = p.pos(sent) # 제외시킬 품사 // 형태소단위로 끊은 형태 (품사가 아직 제외가 안됨)!
# print(pos[0])
# print(pos[1])
# print(pos[2])
# print(pos[3])
# print(pos[4])
# print(pos[5])
# print(pos[6])
# print(pos[7])
# print(pos[8])
# print(pos[9])
# print(pos)
# ret = p.get_keywords(pos, without_tag= False)
# print(pos)
# print(ret)
#
# # 태그 없이 단어만 추출
ret = p.get_keywords(pos, without_tag= True)
print(ret)

