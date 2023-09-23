from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Model
from keras.layers import Input,Conv2D,MaxPooling2D,Activation, Dropout, Flatten, Dense
from keras.layers.merge import concatenate
from keras.callbacks import ReduceLROnPlateau,EarlyStopping,ModelCheckpoint,CSVLogger
from keras.utils import plot_model
import pickle
import tensorflow as tf
import keras
import os
import numpy as np
import random as python_random
import pandas as pd
from matplotlib import pyplot
import itertools  
import pickle

print ('DL_Trained_models.py -a <Path_To_image_specific_directory>')
print('Use -a for Image_data\Image_type1 and Image_data\Image_type2')

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["Afile="])

    for opt, arg in opts:
      if opt == '-h':
         print ('DL_Trained_models.py -a <Path_To_image_specific_directory>' )
         sys.exit()
      elif opt in ("-a", "--Afile"):
         ImageDirectory = arg


    train_datagen = ImageDataGenerator(rescale = 1./255)
    test_datagen = ImageDataGenerator( rescale = 1./255)

    os.chdir(ImageDirectory) # change directory to a particular image type directory


    train_generator = train_datagen.flow_from_directory(
                      ImageDirectory + str("\\") + str("train"), 
                      batch_size = 32, 
                      class_mode = 'categorical', 
                      target_size = (224,224),
                      seed=123)
                      
    validation_generator = test_datagen.flow_from_directory( 
                      ImageDirectory + str("\\") + str("test"), 
                      batch_size = 32, 
                      class_mode = 'categorical', 
                      target_size = (224,224),
                      seed=123)


    target_names = []
    for key in validation_generator.class_indices:
        target_names.append(key)


    from keras.applications.xception import Xception 
    #from keras.applications.mobilenet_v2 import MobileNetV2
    #from keras.applications.inception_resnet_v2 import InceptionResNetV2
    #from keras.applications.densenet import DenseNet169
    #from keras.applications.resnet50 import ResNet50

    base_model = Xception(input_shape = (224,224, 3),include_top = False, weights = 'imagenet')


    for layer in base_model.layers:
        layer.trainable = False

    x = Flatten()(base_model.output)
    x = Dense(1024, activation='relu')(x) 
    x = Dropout(0.2)(x)
    x = Dense(2, activation='sigmoid')(x)

    model = Model(base_model.input, x)    

    model.compile(optimizer = keras.optimizers.Adam(learning_rate=0.0001), loss = 'binary_crossentropy',
                     metrics = [
                     tf.keras.metrics.AUC(), 
                     tf.keras.metrics.Precision(), 
                     tf.keras.metrics.Recall(),
                     tf.keras.metrics.BinaryAccuracy(),
                     ])

    tl_checkpoint_1 = ModelCheckpoint(filepath=(ImageDirectory + str("\\") + str('best_trained_weights.hdf5')),
                                      save_best_only=True,
                                      verbose=1)

    csv_logger = CSVLogger(ImageDirectory + str("\\") +  str("MetricsValues.csv"),separator=",")

    vgghist = model.fit_generator(generator=train_generator,epochs=50,validation_data= validation_generator,callbacks=[tl_checkpoint_1,csv_logger])   

    model.save(ImageDirectory + str("\\") + str("Saved_model.h5"))

if __name__ == "__main__":
    main(sys.argv[1:]) 