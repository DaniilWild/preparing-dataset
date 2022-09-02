import os
import pandas as pd
import shutil
import warnings
from random import randrange
warnings.filterwarnings("ignore")



DIR_MASK = "C://Users/d.tsarkov/Desktop/ddd/"
DIR_IMG = "C://Users/d.tsarkov/Desktop/Цифровой прорыв/RZD_финал/RZD/participants/test/"

df_img = "C://Users/d.tsarkov/Desktop/primer.png"




mass_new_name = []
# for name in df_name_img:

for root, dirs, files in os.walk(DIR_IMG):
    for f in files:
    #print(files)
        shutil.copyfile(df_img, DIR_MASK + f)