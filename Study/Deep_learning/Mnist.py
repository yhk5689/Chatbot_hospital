# 필요한 모듈 임포트
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

# MNIST 데이터셋 가져오기 (28*28) (제공됨) -> numpy 배열형태로 가져옴
(x_train, y_train), (x_test, y_test) = mnist.load_data()    # train - 학습에 필요한 숫자 이미지, ytest - 실제 숫자값
x_train, x_test = x_train / 255.0, x_test / 255.0 # 데이터 정규화
"""
픽셀값이 범위 (0 ~ 255)
but) 신경망 입력층에는 0 ~ 1 사이의 값을 입력 => 정규화 
"""
# plt.imshow(x_train[0], cmap='gray')
# print(y_train[0])

#tf.data를 사용하여 데이터셋을 섞고 배치 만들기
ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000)
train_size = int(len(x_train) * 0.7) # 학습셋:검증셋 = 7:3    # 70%는 실제 학습용 데이터셋, 30%는 검증용 데이터셋
train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).batch(20)

# MNIST 분류 모델 구성
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))    # 2차원 이미지를 1차원으로 평탄화
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(10, activation='softmax'))  # 10개분류, softmax 사용


# 모델 생성
model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# 분류할때 사용하는 손실함수 - sparse
# data의 밀집도를 낮춤, one - hot - encoding -< 0의 갯수를 줄임
# model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 모델 학습
hist = model.fit(train_ds, validation_data=val_ds, epochs=10)

# 모델 평가
print('모델 평가')
model.evaluate(x_test, y_test)

# 모델 정보 출력
model.summary()

# 모델 저장
model.save('mnist_model.h5')

# 학습 결과 그래프
# fig, loss_ax = plt.subplots()
# acc_ax = loss_ax.twinx()
# loss_ax.plot(hist.history['loss'], 'y', label='train loss')
# loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
# acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
# acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')
# loss_ax.set_xlabel('epoch')
# loss_ax.set_ylabel('loss')
# acc_ax.set_ylabel('accuracy')
# loss_ax.legend(loc='upper left')
# acc_ax.legend(loc='lower left')
plt.figure(figsize=(12,4))
plt.subplot(1, 2, 1)
plt.plot(hist.history['loss'], 'b-', label= 'loss')
plt.plot(hist.history['val_loss'], 'r--', label= 'val_loss')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1,2,2)
plt.plot(hist.history['accuracy'], 'g-', label= 'accuracy')
plt.plot(hist.history['val_accuracy'], 'k--', label= 'val_accuracys')
plt.xlabel('Epoch')
plt.ylim(0.7, 1)
plt.legend()
plt.show()