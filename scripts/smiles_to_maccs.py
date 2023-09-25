from rdkit import Chem
from rdkit.Chem import MACCSkeys
import pandas as pd
import os 

print("\n")
print ("smiles_to_maccs.py -i <Input_smiles_file>")

print("Use -i as:")
print(r"Feature_data\train_active_smiles.csv")
print(r"Feature_data\train_inactive_smiles.csv")

print(r"Feature_data\test_active_smiles.csv")
print(r"Feature_data\test_inactive_smiles.csv")



def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
      if opt == '-h':
         print ('smiles_to_maccs.py -i <Input_smiles_file> -o <Output_maccs_file>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         Input_smiles_file = arg
      elif opt in ("-o", "--ofile"):
         Output_maccs_file = arg
         


    k1=pd.read_csv(Input_smiles_file, header = None)

    d1= list()

    for i in range(0,len(k1)):
        ms = Chem.MolFromSmiles(str(k1.iloc[i,0]))
        fps = MACCSkeys.GenMACCSKeys(ms)
        fps1=fps.ToBitString()
        d1.append(fps1)
        
    #l1 = list(fps)
    df = pd.DataFrame(d1)    

    ## write files for directory:
    print(r"If -i is Feature_data\train_active_smiles.csv then output file should be Feature_data\Image_type1\train\active.csv and Feature_data\Image_type2\train\active.csv")
    print(r"If -i is Feature_data\train_inactive_smiles.csv then output file should be Feature_data\Image_type1\train\inactive.csv and Feature_data\Image_type2\train\inactive.csv")
    print(r"If -i is Feature_data\test_active_smiles.csv then output file should be Feature_data\Image_type1\test\active.csv and Feature_data\Image_type2\train\active.csv")
    print(r"If -i is Feature_data\test_inactive_smiles.csv then output file should be Feature_data\Image_type1\test\inactive.csv and Feature_data\Image_type2\train\inactive.csv")

    df.to_csv(Output_maccs_file, header=False, index=False, sep=",")

if __name__ == "__main__":
    main(sys.argv[1:]) 






