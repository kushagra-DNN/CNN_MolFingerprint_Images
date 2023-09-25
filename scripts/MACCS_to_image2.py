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
print(r"data\train\Train_active.csv")
print(r"data\train\Train_inactive.csv")
print(r"data\test\Test_active.csv")
print(r"data\Maybridge\MACCS_maybridge.csv")
print(r"data\test\Test_inactive.csv")

print("\n")
print("Use -o as:")

print(r"data\train\active")
print(r"data\train\inactive")
print(r"data\test\active")
print(r"data\test\inactive")
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







































