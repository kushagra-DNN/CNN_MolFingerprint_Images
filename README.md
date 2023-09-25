# CNN_MolFingerprint_Images

Code for our paper: **Deep learning-based identification and biological evaluation of MAO-B inhibitors**

### STEP 1: Installation
- git clone https://github.com/kushagra-DNN/CNN_MolFingerprint_Images.git <br>
- cd CNN_MolFingerprint_Images <br>
- conda env create -f environment.yaml -n CNN_MolFingerprint_Images <br>
- conda activate CNN_MolFingerprint_Images <br>

### Step 2: Generate folders
Generate folders for training and test set in this format:
```
Image_data\
    Image_type1\
        train\ 
            active\
            inactive\
        test\ 
            active\
            inactive\
  ...
Image_data\
    Image_type2\
        train\ 
            active\
            inactive\
        test\ 
            active\
            inactive\
```

### Step 3: Convert molecular canonical SMILES to MACCS fingerprints
Run:<br>
```
python smiles_to_maccs.py --ifile [Input_smiles_file] --ofile [Output_maccs_file] 
```

### Step 4: Convert MACCS generated files to image type 1 
Run:<br>
```
python MACCS_to_image1.py --ifile [MACCSFilesPath_image1] --ofile [image1_path] 
```

### Step 5: For image type 2 convert MACCS generated files to Matrix of 14*12.  
Run:<br>
```
python MACCS_to_image2.py --ifile [MACCSFilesPath_image2] --ofile [image2_path] 
```
