# -*- coding: utf-8 -*-
"""TumorClassification.ipynb
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H8gA6VZmmep6-gUF98NircTDfPIppg4z

#Importing Libraries
"""
import matplotlib.pyplot as plt
import cv2
import numpy as np
import sys
import keras  #keras creates new Blank ML model
from keras.models import Sequential
import visualkeras #visualizes Keras Model
from tensorflow.keras.models import Sequential             
from tensorflow.keras.layers import Dense, Conv2D, Flatten
from keras.preprocessing.image import  ImageDataGenerator #feeds images into the Keras model
from keras.layers import Conv2D   #makes layers for model to sort images
from keras.layers import Flatten
from keras.layers import Dense

"""Data processing """

gen=ImageDataGenerator(rescale=1//255)
#imageDataGen generates every img in the folder at a time and takes input for rescale value
#creates new scale for image colors to normalize data and make it all significant

gen

#flow_from_directory function- connects ImageDataGenerator with all the images in file
trainingData=gen.flow_from_directory('C:\\Users\\Krishna.000\\Downloads\\BrainTumorData\\Training',target_size=(128,128))

#connects ImageDataGenerator to testing using the same function
testingData=gen.flow_from_directory('C:\\Users\\Krishna.000\\Downloads\\BrainTumorData\\Training',target_size=(128,128))

#now we build the NN
#step 1: define a model (empty model object from Sequential class) (below)
#2: add layers by using .add()

model = Sequential() #creates new sequential

model.add(Conv2D(2,kernel_size=(3,3), activation='sigmoid', input_shape=(128,128,3))) #creates a new layer

model.add(Conv2D(2,kernel_size=(3,3), activation='sigmoid')) #creates another layer, copies previous shappe by defualt

model.add(Flatten())#creates new layer to flatten image and make numbers into a vector

model.add(Dense(64,activation='sigmoid'))
#adds dense layer(non-convolution)

model.add(Dense(4,activation='softmax'))
#adds output(final) layer with number of outputs(4)

model.summary() #summarizes model and shows what it looks like

model.summary()#Param

"""training the ai"""

model.compile(loss='binary_crossentropy',optimizer='adam')     #defines err function and uses an optimizer called Adam

history=model.fit(trainingData,validation_data=testingData,epochs=5) #trains ML model 2 times, adjust epochs and other stuff here

visualkeras.layered_view(model, legend = True) #visualize model