import os
import numpy as np
from PIL import Image
from PIL import Image as im
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


print ('MACCS_to_image2.py -i <MACCSFilesPath_image2> -o <image2_path>')
print("\n")

print ("Use -i as:") 

print(r"Feature_data\Image_type2\Train\Matrix_actives")
print(r"Feature_data\Image_type2\Train\Matrix_inactives")
print(r"Feature_data\Image_type2\Test\Matrix_actives")
print(r"Feature_data\Image_type2\test\Matrix_inactives")
print(r"Feature_data\Image_type2\test\Maybridge\Matrix")

print("\n")
print("Use -o as:")

print(r"Image_data\Image_type2\train\active")
print(r"Image_data\Image_type2\train\inactive")
print(r"Image_data\Image_type2\test\active")
print(r"Image_data\Image_type2\test\inactive")

print("\n")

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
      if opt == '-h':
         print ('MACCS_to_image2.py -i <MACCSFilesPath_image2> -o <image2_path>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         MACCSFilesPath_image2 = arg
      elif opt in ("-o", "--ofile"):
         image2_path = arg
         

    px = 1/plt.rcParams['figure.dpi']  
    plt.figure(figsize=(224*px, 224*px)) 


    for i in range(0,len(MACCSFilesPath_image2)):
        k2= pd.read_csv(MACCSFilesPath_image2 + str(i+1) + ".csv", header = None)

        sns.heatmap( k2, cmap = 'gray', cbar=False, yticklabels=False, xticklabels=False, linewidths=0.005, linecolor="green")
        plt.tight_layout(pad=0)
        plt.savefig(image2_path + "May_" + str(i+1) + ".png") 
        plt.clf()

if __name__ == "__main__":
    main(sys.argv[1:]) 







































