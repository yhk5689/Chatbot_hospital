import numpy as np
import tensorflow as tf
x = np.array([[1,1],[1,0],[0,1],[0,0]])
y = np.array([[0],[1],[1],[0]])

# keras - 신경망을 사용하기 위한 API
model = tf.keras.Sequential([   # 신경망 모델 정의
    tf.keras.layers.Dense(units= 2, activation= 'sigmoid', input_shape=(2,)),   # 뉴런 갯수, 활성화함수, 입력은 2개
    tf.keras.layers.Dense(units= 1, activation= 'sigmoid')  # Dense - 모든 입력이 다 연결 # Sequential - 직선형구조
])
# compile - 학습 준비, 실행
model.compile(optimizer= tf.keras.optimizers.SGD(lr=0.1), loss= 'mse')  # optimizer = 경사하강법(오차최소) SGD = 알고리즘 이름, lr = 학습률, loss = 오차함수, mse - 평균제곱오차
# summary - 신경망 구조
model.summary()

history = model.fit(x, y, epochs=2000, batch_size=1)
model.predict(x)
print("입력 : {0}  = {1}".format(x[0], model.predict(x)[0]))
print("입력 : {0}  = {1}".format(x[1], model.predict(x)[1]))
print("입력 : {0}  = {1}".format(x[2], model.predict(x)[2]))
print("입력 : {0}  = {1}".format(x[3], model.predict(x)[3]))

