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
python_random.seed(10)

print("\n")
print ("CNN.py -a <Path_To_image_specific_directory>")
print("Use -a as")

print(r"Image_data\Image_type1")
print(r"Image_data\Image_type2")
print("\n")

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["Afile="])

    for opt, arg in opts:
      if opt == '-h':
         print ('CNN.py -a <Path_To_image_specific_directory>' )
         sys.exit()
      elif opt in ("-a", "--Afile"):
         ImageDirectory = arg
         
         
         
    train_datagen =ImageDataGenerator( rescale=1./255)
    test_datagen = ImageDataGenerator( rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
              str(ImageDirectory + str("\\") + str("train")),  
              target_size=(224,224),
              batch_size=32,
              class_mode='categorical')

    test_generator =test_datagen.flow_from_directory(
              str(ImageDirectory + str("\\") + str("test")),  
              target_size=(224,224),
              batch_size=32,
              class_mode='categorical')  

    target_names = []
    for key in test_generator.class_indices:
        target_names.append(key)


    def CNN_architecture(layer_in, f1, f2_in, f2_out, f3_in, f3_out, f4_out):
        conv1 = Conv2D(f1, (1,1), padding='same', activation='relu')(layer_in)

        conv3 = Conv2D(f2_in, (1,1), padding='same', activation='relu')(layer_in)
        conv3 = Conv2D(f2_out, (3,3), padding='same', activation='relu',kernel_regularizer =tf.keras.regularizers.l2( l=0.0001))(conv3)

        conv5 = Conv2D(f3_in, (1,1), padding='same', activation='relu')(layer_in)
        conv5 = Conv2D(f3_out, (5,5), padding='same', activation='relu',kernel_regularizer =tf.keras.regularizers.l2( l=0.0001))(conv5)

        pool = MaxPooling2D((3,3), strides=(1,1), padding='same')(layer_in)
        pool = Conv2D(f4_out, (1,1), padding='same', activation='relu',kernel_regularizer =tf.keras.regularizers.l2( l=0.0001))(pool)

        layer_out = concatenate([conv1, conv3, conv5, pool], axis=-1)
        return layer_out

    visible = Input(shape=(224, 224, 3))
    layer = CNN_architecture(visible, 25,30, 40, 30, 40,45)

    model = keras.models.Model(inputs=visible, outputs=layer)
    model.summary()


    Model = Sequential()
    Model.add(model)

    Model.add(Flatten())  
    Model.add(Dense(2))
    Model.add(Activation('sigmoid'))


    os.chdir(ImageDirectory)

    Model.compile(optimizer = keras.optimizers.Adam(learning_rate=0.0001), loss = 'binary_crossentropy',
                     metrics = [
                     tf.keras.metrics.AUC(), 
                     tf.keras.metrics.Precision(), 
                     tf.keras.metrics.Recall(),
                     tf.keras.metrics.BinaryAccuracy()
                     ])


    tl_checkpoint_1 = ModelCheckpoint(filepath='best_trained_weights.hdf5',
                                      save_best_only=True,
                                      verbose=1)



    csv_logger = CSVLogger(ImageDirectory + str("\\") +  str("MetricsValues.csv"),separator=",")
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.0001, verbose=1)    

    vgghist = Model.fit_generator(generator=train_generator,epochs=50,validation_data= test_generator,callbacks=[tl_checkpoint_1,csv_logger,reduce_lr])   

    model.save(ImageDirectory + str("\\") + str("Saved_model.h5"))

if __name__ == "__main__":
    main(sys.argv[1:]) 
    
    
