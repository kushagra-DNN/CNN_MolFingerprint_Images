from matplotlib import pyplot as plt
from pylab import *
import os
import pandas as pd
import seaborn as sns
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageColor

print ('MACCS_to_image1.py -i <MACCSFilesPath_image1> -o <image1_path>')
print ("Use -i as:")

########## NOTE ########
#For Active\Inactive classes images in train set:
# Use active, active_156 for generating images for the folder Feature_data\Image_type1\train\active and Feature_data\Image_type1\test\active
# Use inactive, inactive_156 for generating images for the folder Feature_data\Image_type1\train\inactive and Feature_data\Image_type1\test\inactive
############ ###########

#Feature_data\Image_type1\train\active.csv
#Feature_data\Image_type1\train\active_156.csv
#Feature_data\Image_type1\train\inactive.csv
#Feature_data\Image_type1\train\inactive_156.csv


#Feature_data\Image_type1\test\active.csv
#Feature_data\Image_type1\test\active_156.csv
#Feature_data\Image_type1\test\inactive.csv
#Feature_data\Image_type1\test\inactive_156.csv

print ("Use -o as:")

#train 
#Image_data\Image_type1\train\active
#Image_data\Image_type1\train\inactive

#test
#Image_data\Image_type1\test\active
#Image_data\Image_type1\test\inactive


def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
      if opt == '-h':
         print ('MACCS_to_image1.py -i <MACCSFilesPath_image1> -o <image1_path>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         MACCSFilesPath_image1 = arg
      elif opt in ("-o", "--ofile"):
         image1_path = arg

os.chdir(image1_path)

k1=pd.read_csv(MACCSFilesPath_image1, header =None) # input file active_156.csv/inactive_156.csv 
kk1=pd.read_csv(MACCSFilesPath_image1, header =None) # input file active.csv/inactive.csv

for i in range(0,len(k1)):
    k2 = (k1.iloc[i,:])
    
    img = Image.new(mode="RGBA", size=(224,224), color='black')  ## maccs done for 150*3390

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(r'C:\\Windows\\Fonts\\ARLRDBD.ttf',15) 

        
    a3=0
    b3=1
    c3=2
    d3=3
    e3=4
    f3=5
    g3=6
    h3=7
    i3=8
    j3=9
    k3=10
    l3=11
    
    m=9
    
    for j in range(0,13):
        draw.text((8, m), str(k2[a3]), font = font, fill = (255,255,255))     
        draw.text((26, m), str(k2[b3]), font = font, fill = (255,255,255))    
        draw.text((44, m), str(k2[c3]), font = font, fill = (255,255,255))    
        draw.text((62, m), str(k2[d3]), font = font, fill = (255,255,255))    
        draw.text((80, m), str(k2[e3]), font = font, fill = (255,255,255))    
        draw.text((98, m), str(k2[f3]), font = font, fill = (255,255,255))    
        draw.text((116, m), str(k2[g3]), font = font, fill = (255,255,255))    
        draw.text((134, m), str(k2[h3]), font = font, fill = (255,255,255)) 
        draw.text((152, m), str(k2[i3]), font = font, fill = (255,255,255))
        draw.text((170, m), str(k2[j3]), font = font, fill = (255,255,255)) 
        draw.text((188, m), str(k2[k3]), font = font, fill = (255,255,255)) 
        draw.text((206, m), str(k2[l3]), font = font, fill = (255,255,255)) 

        a3=a3+12
        b3=b3+12
        c3=c3+12
        d3=d3+12
        
        e3=e3+12
        f3=f3+12
        g3=g3+12
        h3=h3+12
        i3=i3+12
        j3=j3+12
        k3=k3+12
        l3=l3+12

        m=m+14.5
    draw.text((8, 197), str(kk1.iloc[i,156]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((26, 197), str(kk1.iloc[i,157]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((44, 197), str(kk1.iloc[i,158]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((62, 197), str(kk1.iloc[i,159]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((80, 197), str(kk1.iloc[i,160]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((98, 197), str(kk1.iloc[i,161]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((116, 197), str(kk1.iloc[i,162]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((134, 197), str(kk1.iloc[i,163]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((152, 197), str(kk1.iloc[i,164]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((170, 197), str(kk1.iloc[i,165]), font = font, fill = (255,255,255))    ## start 390 for 400*390
    draw.text((188, 197), str(kk1.iloc[i,166]), font = font, fill = (255,255,255))    ## start 390 for 400*390
            
        

    plt.tight_layout(pad=0)
    plt.axis('off')
    img.save("active_" + str(i+1) + ".png") # set output file images names with a format active_/inactive_
    plt.clf()


