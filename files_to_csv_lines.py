import os
import pandas as pd
import shutil
import warnings
warnings.filterwarnings("ignore")


def class_img(dir_name):
    if dir_name == "no_objects":
        obj_class = int(0)
    elif dir_name == "yes_objects":
        obj_class = int(1)
    elif dir_name == "poor_quality":
        obj_class = int(2)

    return obj_class

DIR_TEST = "C://Users/d.tsarkov/Desktop/УФА/test/"
DIR_TRAIN = "C://Users/d.tsarkov/Desktop/УФА/train/"
FILE_DIR = "C://Users/d.tsarkov/Downloads/Цифровой прорыв"
DIR_CSV = "C://Users/d.tsarkov/Desktop/УФА/"

df_test = pd.DataFrame({'ID_img': [], 'class': []})
df_train = pd.DataFrame({'ID_img': [], 'class': []})

for root, dirs, files in os.walk(FILE_DIR):

    test_index = int(len(files) * 0.3)

    test_files = files[:test_index]
    train_files = files[test_index:]



    for file_name in test_files:
        dir_name = root.split("\\")[-1]
        obj_class = class_img(dir_name)

        df_test = df_test.append({'ID_img': file_name, 'class': obj_class}, ignore_index=True)
        shutil.copyfile(root+"/"+file_name, DIR_TEST+file_name)
        #print(root+"/"+file_name, DIR_TEST+file_name)

    for file_name in train_files:
        dir_name = root.split("\\")[-1]
        obj_class = class_img(dir_name)

        df_train = df_train.append({'ID_img': file_name, 'class': obj_class}, ignore_index=True)
        shutil.copyfile(root+"/"+file_name, DIR_TRAIN+file_name)

    print(df_test)

    df_test = df_test.sample(frac=1)
    df_train = df_train.sample(frac=1)

    df_test.to_csv(DIR_CSV + 'test.csv', index=False)
    df_train.to_csv(DIR_CSV + 'train.csv', index=False)

    print("df_test shape", df_test.shape)
    print("df_train shape", df_train.shape)