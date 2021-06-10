from keras.datasets import mnist
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images, test_images, train_labels, test_labels = train_test_split(
    train_images, train_labels,
    test_size=0.3, random_state=42
)

train_images = train_images.reshape(-1, 28 * 28)
train_images = train_images / 255.0

test_images = test_images.reshape(-1, 28 * 28)
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

dense1 = layers.Dense(512, activation='relu', input_shape=(28 * 28,), name="hidden1")
dense2 = layers.Dense(10, activation='softmax', name="output")
model = models.Sequential([dense1, dense2])

model.compile(optimizer='AdaGrad', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc  : ', test_acc)
