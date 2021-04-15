
from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# MNIST 데이터셋 가져오기
_, (x_test, y_test) = mnist.load_data() # 이미 학습된 모델을 불러와서 사용하기 때문에 test data만 가져옴
x_test = x_test / 255.0 # 데이터 정규화

# 모델 불러오기
model = load_model('mnist_model.h5')
model.summary()
model.evaluate(x_test, y_test, verbose=2)   #verbose 는  진행상황을 보여줌

# 테스트셋에서 20번째 이미지 출력
plt.imshow(x_test[19], cmap="gray")
plt.show()

# 테스트셋의 20번째 이미지 클래스 분류
picks = [19]
predict = model.predict_classes(x_test[picks])
print("손글씨 이미지 예측값 : ", predict)