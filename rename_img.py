import os
import pandas as pd
import shutil
import warnings
from random import randrange
warnings.filterwarnings("ignore")



DIR_TEST = "C://Users/d.tsarkov/Desktop/УФА_финал/participants/test/"
DIR_TEST_NEW = "C://Users/d.tsarkov/Desktop/УФА_финал/participants/test_new/"

df_ground_truth = "C://Users/d.tsarkov/Desktop/УФА_финал/org/ground_truth.csv"
df_ground_truth_new = "C://Users/d.tsarkov/Desktop/УФА_финал/org/ground_truth_new.csv"


df_gt = pd.read_csv(df_ground_truth)

df_name_img = df_gt.ID_img.values
df_class_img = df_gt["class"].values

mass_new_name = []
for name in df_name_img:
    new_name = str(randrange(0,99999999999))+"_"+str(randrange(0,99999999999))+"_" + str(randrange(0,99999999999)) + "_" + str(randrange(0,9))
    mass_new_name.append(new_name)

    shutil.copyfile(DIR_TEST + name, DIR_TEST_NEW + new_name+ "." + name.split(".")[-1])

df_gt.ID_img = mass_new_name
df_gt = df_gt.sample(frac=1)

print(df_gt.head(5))

df_gt.to_csv(df_ground_truth_new, index=False)

