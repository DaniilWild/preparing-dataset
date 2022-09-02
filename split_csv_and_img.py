import os
import pandas as pd
import warnings
from random import randrange
warnings.filterwarnings("ignore")
import shutil

#Из файла с названием картинок и папки делаем тест и треин

# Оригинал
DIR_img = "C://Users/d.tsarkov/Desktop/База Данных КАМИС/База данных КАМИС Фотографии/Новая папка/"
df_img = "C://Users/d.tsarkov/Desktop/Дорожные знаки/data_sings.csv"

# Попилинный датасет
DIR_img_train = "C://Users/d.tsarkov/Desktop/Пермский музей/participants/train/"
DIR_img_test = "C://Users/d.tsarkov/Desktop/Пермский музей/participants/test/"

# Новые файлы
# df_test = "C://Users/d.tsarkov/Desktop/Дорожные знаки/Итог/test.csv"
# df_train = "C://Users/d.tsarkov/Desktop/Дорожные знаки/Итог/train.csv"


# df_gt = pd.read_csv(df_img)
# df_gt = df_gt.sample(frac=1)
#
# df_gt[:388].to_csv(df_test, index = False)
# df_gt[388:].to_csv(df_train, index = False)

df_train = pd.read_csv("C://Users/d.tsarkov/Desktop/Пермский музей/participants/train.csv")
df_test = pd.read_csv("C://Users/d.tsarkov/Desktop/Пермский музей/org/ground_truth.csv")


for name in df_test.object_img.values:
    shutil.copyfile(DIR_img +"  (" + str(name)+").png", DIR_img_test + str(name)+".png")

for name in df_train.object_img.values:
    shutil.copyfile(DIR_img + "  (" + str(name)+").png", DIR_img_train + str(name)+".png")

# for name in df_gt[388:].img.values:
#     shutil.copyfile(DIR_img + name, DIR_img_train + name)
#
# df_gt.ID_img = mass_new_name
# df_gt = df_gt.sample(frac=1)
#
# df_gt.to_csv(df_ground_truth_new, index=False)

