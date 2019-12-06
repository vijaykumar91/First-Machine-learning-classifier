import tensorflow as ts
from tensorflow import keras

fashion_mnist=keras.datasets.fashion_mnist
(train_images,train_labels),(test_images, test_labels)=fashion_mnist.load_data()


#----------------- Keras-------------------#
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

model = tf.keras.Sequential()
# Adds a densely-connected layer with 64 units to the model:
model.add(layers.Dense(64, activation='relu'))
# Add another:
model.add(layers.Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(layers.Dense(10, activation='softmax'))