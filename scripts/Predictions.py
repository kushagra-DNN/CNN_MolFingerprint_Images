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
import sys
python_random.seed(10)

print("\n")
print ('Predictions.py -d <DL_Models> -t <TrainingImageFilesPath> -m <MaybridgeImageFilePath> -mo <PredictionsResultPath>\n')
print("For image type1:, Give -d as:")

print(r"DL_Models_Image_type1\CNN_architecture\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type1\DenseNet169\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type1\Inception_Resnet\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type1\MobileNet\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type1\ResNet50\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type1\Xception\best_trained_weights.hdf5") 

print("\n")

print("For image type2:, Give -d as:")

print(r"DL_Models_Image_type2\CNN_architecture\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type2\DenseNet169\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type2\Inception_Resnet\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type2\MobileNet\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type2\ResNet50\best_trained_weights.hdf5") 
print(r"DL_Models_Image_type2\Xception\best_trained_weights.hdf5") 


print("\n")

print("For image type1:, Give -t as:")
print(r"Image_data\Image_type1\train")

print("\n")

print("For image type2:, Give -t as:")
print(r"Image_data\Image_type2\train")



print("\n")

print("For image type1:, Give -m as:")
print(r"Image_data\Image_type1\Maybridge")

print("\n")

print("For image type2:, Give -m as:")
print(r"Image_data\Image_type2\Maybridge")

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["Dfile=", "Tfile=", "Mfile=", "Mofile="])

    for opt, arg in opts:
      if opt == '-h':
         print ('Predictions.py -d <DL_Models> -t <TrainingImageFilesPath> -m <MaybridgeImageFilePath> -mo <PredictionsResultPath>\n')
         sys.exit()
      elif opt in ("-d", "--Dfile"):
         DL_Models = arg
      elif opt in ("-t", "--Tfile"):
         TrainingImageFilesPath = arg
      elif opt in ("-m", "--Mfile"):
         MaybridgeImageFilePath = arg
      elif opt in ("-mo", "--Mofile"):
         PredictionsResultPath = arg
         
         
    train_datagen =ImageDataGenerator( rescale=1.0/255)
    validation_datagen = ImageDataGenerator( rescale=1.0/255 ) 
        
    model1=tf.keras.models.load_model(DL_Models)

    train_generator = train_datagen.flow_from_directory(
      TrainingImageFilesPath,
      target_size=(224,224),
      batch_size=32,
      class_mode='categorical')  

         
    validation_generator =validation_datagen.flow_from_directory(
      MaybridgeImageFilePath,    
      target_size=(224, 224),
      batch_size=1,  #color_mode="rgb",
      class_mode='categorical',
      shuffle=False )  
  
    filenames = validation_generator.filenames
    nb_samples = len(filenames)

    validation_generator.reset()

    predict = model1.predict_generator(validation_generator,verbose=1,steps=nb_samples)
    from sklearn.metrics import confusion_matrix

    predicted_class_indices=np.argmax(predict,axis=1)

    labels = (train_generator.class_indices)

    labels = dict((v,k) for k,v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]


    results=pd.DataFrame({"Filename":filenames,
                      "Predictions":predictions})
    results.to_csv(PredictionsResultPath + str("Predictions.csv"))
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
