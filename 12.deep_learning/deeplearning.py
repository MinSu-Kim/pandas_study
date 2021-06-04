# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 30)  # 출력할 최대 열의 개수
pd.set_option('display.width', 600)  # 콘솔 출력 너비

# MNIST(손글씨) 데이터셋 불러오기 훈련세트와 테스트세트로 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

from sklearn.model_selection import train_test_split

train_images, test_images, train_labels, test_labels = train_test_split(train_images, train_labels, test_size=0.3, random_state=42)

# 배열 크기 , 타입 확인
print("배열 크기 , 타입 확인")
print("train_images shape = ", train_images.shape)
print("train_images dtype = ", train_images.dtype)
print("len(train_images) ", len(train_images), end='\n\n')
print("train_labels shape = ", train_labels.shape)
print("train_labels dtype = ", train_labels.dtype)
print("len(train_labels) ", len(train_labels), end='\n\n')

print("test_images shape = ", test_images.shape)
print("test_images dtype = ", test_images.dtype)
print("len(test_images) ", len(test_images), end='\n\n')
print("test_labels shape = ", test_labels.shape)
print("test_labels dtype = ", test_labels.dtype)
print("len(test_labels) ", len(test_labels), end='\n\n')

# 0-19 테스트 이미지 출력
count = 0
for i in range(20):
    count += 1
    plt.subplot(4, 5, count)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.title("images[{}]".format(i))
plt.tight_layout()
plt.show()

# 0-19 레이블값 출력
print("0-19 레이블값 출력 ", [train_labels[i] for i in range(10)], end='\n\n')

# 5번째 이미지및 레이블 출력
print("5번째 이미지", pd.DataFrame(train_images[4]), sep='\n')
print("5번째 레이블", train_labels[4], sep='\n', end='\n\n')

# 레이블당 샘플 개수 확인
ret_counts = np.unique(train_labels, return_counts=True)
print(ret_counts)
print("샘플 개수 : ", np.sum(ret_counts[1]), end='\n\n')


# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
# train이미지는 [0-255]사이의 값인 uint8 타입의 (60000, 28 , 28) 크기를 가지 배열을  -> 0과 1사이의 값을 가지는 float32타입의 (60000, 28*28)크기인 배열로 변경
# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype('float32') / 255
train_images = train_images.reshape(-1, 28 * 28)
train_images = train_images / 255.0

test_images = test_images.reshape(-1, 28 * 28)
test_images = test_images.astype('float32') / 255

# 배열 크기 , 타입 확인
print("모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링후 배열크기 타입 확인")
print("train_images shape = ", train_images.shape, '\n', "train_images dtype = ", train_images.dtype)
print(train_images[4])
print("test_images shape = ", test_images.shape, '\n', "test_images dtype = ", test_images.dtype)
print(test_images[4])
print()


# 레이블을 범주형으로 원핫 인코딩
print("레이블을 범주형으로 원핫 인코딩 전", train_labels.shape, pd.DataFrame(train_labels).head(), sep='\n', end='\n\n')
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

print("레이블을 범주형으로 원핫 인코딩 후", train_labels.shape, pd.DataFrame(train_labels).head(), sep='\n', end='\n\n')


# 모델 구조 정의하기 (신경망 생성, 여기에서는 Sequential 클래스 사용)
# 뉴런의 개수 : 512, 뉴련출력에 적용할 함수 : relu, 입력크기(28*28) 밀집층 추가( 완전연결층 )
dense1 = layers.Dense(100, activation='relu', input_shape=(28 * 28,), name="hidden1")
# 뉴런의 개수 : 10, 뉴련출력에 적용할 함수 : softmax, 입력 앞의 층 (은닉층)
dense3 = layers.Dense(50, activation='relu', name="hidden2")
drop4 = layers.Dropout(0.4) # overfit 감소 40%
dense2 = layers.Dense(10, activation='softmax', name="output")
model = models.Sequential([dense1, dense3, drop4, dense2])

# model 요약
print("model 요약")
model.summary()
print()


# 모델 컴파일 하기

"""
손실 함수 (loss): 손실 함수는 값을 예측하려할 때 데이터에대한 예측값과 실제의 값을 비교하는 함수로 모델을 훈련시킬 때 
                 오류를 최소화 시키기 위해 사용
        categorical_crossentropy: 여러 개의 카테고리가 있는 다중 분류, 
        binary_crossentropy:이진 분류, 
        mse(mean squared eror, mae) : 회귀문제, 
        시퀀스 학습 문제: CTC 언어인식)
옵티마이저 (optimizer) :  경사 하강법(rmsprop, sgd, adagrad, Adam, Nadam, AdaMax) 옵티마이저에 의해 결정.
"""

# model.compile(optimizer='Nadam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='AdaMax', loss='categorical_crossentropy', metrics=['accuracy'])
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='AdaGrad', loss='categorical_crossentropy', metrics=['accuracy'])


# fit() 메서드로 모델 훈련 시키기 : 128개씩 5번 반복
print("fit() 메서드로 모델 훈련 시키기 : 128개씩 10번 반복")
history = model.fit(train_images, train_labels, epochs=10, batch_size=128, validation_data=(test_images, test_labels))
# model.fit(train_images, train_labels, epochs=5)
print()

# 테스트 데이터로 정확도 측정하기
print("테스트 데이터로 정확도 측정하기")
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc  : ', test_acc)
print('test_loss : ', test_loss, end='\n\n')

####################################################
print("손실과 정확도 측정", history.history.keys())

fig = plt.figure()
axe1 = fig.add_subplot(2, 1, 1)

axe1.plot(history.history["loss"], label='train', marker="o")
axe1.plot(history.history["val_loss"], label='test', marker="o")
axe1.legend(loc='best')
axe1.set_xlabel('epoch')
# axe1.set_xticks([0, 1, 2, 3, 4])
# axe1.set_xlim([0, 4])
axe1.set_ylabel('loss')
axe1.set_title('loss rate')

axe2 = fig.add_subplot(2, 1, 2)
axe2.plot(history.history["accuracy"], label='train', marker="o")
axe2.plot(history.history["val_accuracy"], label='test', marker="o")
axe2.legend(loc='best')
axe2.set_xlabel('epoch')
axe2.set_ylabel('accuracy')
# axe2.set_xticks([0, 1, 2, 3, 4])
# axe2.set_xlim([0, 4])
axe2.set_title('accuracy rate')

fig.tight_layout()
plt.show()



# ####################################################
import random


predicted_result = model.predict(test_images)

predicted_labels = np.argmax(predicted_result, axis=1)
test_labels = np.argmax(test_labels, axis=1)

wrong_result = []

for n in range(0, len(test_labels)):
    if predicted_labels[n] != test_labels[n]:
        wrong_result.append(n)

print('wrong_result.count() : ', len(wrong_result))

samples = random.choices(population=wrong_result, k=16)

count = 0
nrows = ncols = 4
plt.figure(figsize=(12,8))

for n in samples:
    count += 1
    plt.subplot(nrows, ncols, count)
    plt.imshow(test_images[n].reshape(28, 28), cmap='Greys', interpolation='nearest')
    tmp = "Label:" + str(test_labels[n]) + ", Prediction:" + str(predicted_labels[n])
    plt.title(tmp)

plt.tight_layout()
plt.show()
