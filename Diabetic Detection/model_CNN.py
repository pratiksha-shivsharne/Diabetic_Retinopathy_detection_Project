# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:11:21 2021
Updated for TensorFlow 2.x compatibility

@author: srcdo
"""

# Updated imports for modern TensorFlow/Keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.optimizers import SGD, RMSprop, Adam
from tensorflow.keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from PIL import Image
from numpy import *

# SKLEARN
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# input image dimensions
img_rows, img_cols = 64, 64

# number of channels
img_channels = 3

#%%
#  data

path1 = r'C:\Users\TUF GAMING\Downloads\100%code\100%code\Diabetic Detection\Diabetic Detection\training_set\5'    # path of folder of images    
path2 = r'C:\Users\TUF GAMING\Downloads\100%code\100%code\Diabetic Detection\Diabetic Detection\test_set\5'  # path of folder to save images    

# Create output directory if it doesn't exist
if not os.path.exists(path2):
    os.makedirs(path2)

listing = os.listdir(path1)
num_samples = len(listing)  # Use len() instead of size()
print(num_samples)

for file in listing:
    im = Image.open(os.path.join(path1, file))  # Use os.path.join for better path handling
    img = im.resize((img_rows, img_cols))
    gray = img.convert(mode='RGB')
    gray.save(os.path.join(path2, file), "JPEG")

imlist = os.listdir(path2)

# Fix the path reference issue
im1 = array(Image.open(os.path.join(path2, imlist[0])))  # Use path2 instead of hardcoded path
m, n = im1.shape[0:2]  # get the size of the images
imnbr = len(imlist)  # get the number of images

# Uncomment and modify the following sections as needed for your training

# # create matrix to store all flattened images
# immatrix = array([array(Image.open(os.path.join(path2, im2))).flatten()
#                   for im2 in imlist], 'f')
               
# label = np.ones((num_samples,), dtype=int)
# label[0:245] = 0
# label[245:288] = 1

# data, Label = shuffle(immatrix, label, random_state=2)
# train_data = [data, Label]

# print("Train data shape:", train_data[0].shape)
# print("Train labels shape:", train_data[1].shape)

# #%%

# # batch_size to train
# batch_size = 32
# # number of output classes
# nb_classes = 7
# # number of epochs to train
# nb_epoch = 100

# # number of convolutional filters to use
# nb_filters = 64
# # size of pooling area for max pooling
# nb_pool = 2
# # convolution kernel size
# nb_conv = 3

# #%%
# (X, y) = (train_data[0], train_data[1])

# # STEP 1: split X and y into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # For RGB images, use 3 channels instead of 1
# X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 3)
# X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 3)

# X_train = X_train.astype('float32')
# X_test = X_test.astype('float32')

# X_train /= 255
# X_test /= 255

# print('X_train shape:', X_train.shape)
# print(X_train.shape[0], 'train samples')
# print(X_test.shape[0], 'test samples')

# # convert class vectors to binary class matrices
# Y_train = to_categorical(y_train, nb_classes)  # Updated function name
# Y_test = to_categorical(y_test, nb_classes)

# print("Label shape:", Y_train[0])

# #%%

# # Build CNN model
# model = Sequential()

# # First Convolution Block
# model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_rows, img_cols, 3)))
# model.add(Conv2D(32, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

# # Second Convolution Block
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

# # Fully Connected Layer
# model.add(Flatten())
# model.add(Dense(512, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(nb_classes, activation='softmax'))

# # Compile model
# LEARN_RATE = 1.0e-4
# adam = Adam(learning_rate=LEARN_RATE, beta_1=0.9, beta_2=0.999, epsilon=None)  # Updated parameter name
# model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

# # Callbacks
# from tensorflow.keras.callbacks import ModelCheckpoint, CSVLogger, EarlyStopping

# filename = 'model_train_new.csv'
# csv_log = CSVLogger(filename, separator=',', append=False)

# early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1, mode='min')
# checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True, mode='auto', verbose=1)

# callbacks_list = [csv_log, early_stopping, checkpoint]

# # Train model
# hist = model.fit(X_train, Y_train, 
#                  batch_size=batch_size, 
#                  epochs=nb_epoch,
#                  verbose=1, 
#                  validation_data=(X_test, Y_test),
#                  callbacks=callbacks_list)

# # Save model
# model.save('best_model.h5')

# # Visualizing losses and accuracy
# train_loss = hist.history['loss']
# val_loss = hist.history['val_loss']
# train_acc = hist.history['accuracy']
# val_acc = hist.history['val_accuracy']
# xc = range(len(train_loss))

# plt.figure(1, figsize=(7, 5))
# plt.plot(xc, train_loss)
# plt.plot(xc, val_loss)
# plt.xlabel('Number of Epochs')
# plt.ylabel('Loss')
# plt.title('Train Loss vs Val Loss')
# plt.grid(True)
# plt.legend(['train', 'val'])
# plt.show()

# plt.figure(2, figsize=(7, 5))
# plt.plot(xc, train_acc)
# plt.plot(xc, val_acc)
# plt.xlabel('Number of Epochs')
# plt.ylabel('Accuracy')
# plt.title('Train Accuracy vs Val Accuracy')
# plt.grid(True)
# plt.legend(['train', 'val'], loc=4)
# plt.show()

# #%%      

# # Evaluate model
# score = model.evaluate(X_test, Y_test, verbose=0)
# print('Test score:', score[0])
# print('Test accuracy:', score[1])

# # Make predictions
# Y_pred = model.predict(X_test)
# y_pred = np.argmax(Y_pred, axis=1)

# # Confusion Matrix
# from sklearn.metrics import classification_report, confusion_matrix

# target_names = ['class 0(Normal)', 
#                 'class 1(Abnormal_Agenesis_of_the_Corpus_Callosum)',
#                 'class 2(Abnormal_Agenesis_of_the_Septi_Pellucidi)',
#                 'class 3(Abnormal_Cerebellar_Hypoplasia)',
#                 'class 4(Abnormal_Dandy_Walker_VariantMalformation)',
#                 'class 5(Abnormal_Megacisterna_Magna)',
#                 'class 6(Abnormal_Venous_Malformation)']

# print(classification_report(np.argmax(Y_test, axis=1), y_pred, target_names=target_names))
# print(confusion_matrix(np.argmax(Y_test, axis=1), y_pred))

# # Save weights
# fname = "weights-Test-CNN.h5"
# model.save_weights(fname, overwrite=True)

# # Load weights (when needed)
# # fname = "weights-Test-CNN.h5"
# # model.load_weights(fname)

print("Image preprocessing completed successfully!")