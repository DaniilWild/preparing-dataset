import os
import shutil
import warnings
import random

warnings.filterwarnings("ignore")

DIR1 = "C://Users/d.tsarkov/Desktop/Tasks/Task1/1/" # Изначальные папки с фалами впермешку
DIR2 = "C://Users/d.tsarkov/Desktop/Tasks/Task1/2/"
DIR3 = "C://Users/d.tsarkov/Desktop/Tasks/Task1/hard/"

DIR_json = "C://Users/d.tsarkov/Desktop/ddd/json/" # Промежуточные разделенные файлы
DIR_img = "C://Users/d.tsarkov/Desktop/ddd/img/"

DIR_test = "C://Users/d.tsarkov/Desktop/МФТИ/participants/test/" # Конечная точка назначения
DIR_ground = "C://Users/d.tsarkov/Desktop/МФТИ/org/ground_truth/"

# id = 1
# for dir in [DIR1,DIR2,DIR3]:
#     for _, _, files in os.walk(dir):
#         for x in files:
#             if x.endswith(".json"):
#                 shutil.copyfile(dir + x.split(".")[0] + ".png", DIR_img + str(id) + ".png")
#                 shutil.copyfile(dir + x, DIR_json + str(id) + ".json")
#                 id += 1


random_files = random.sample(os.listdir(DIR_json), 400)

for f in random_files:
#     # print(DIR_json+ f,DIR_ground)
#     # print(DIR_json+ f.split(".")[0] + ".png",)
    shutil.move(DIR_json+ f, DIR_ground)
    shutil.move(DIR_img + f.split(".")[0] + ".png",  DIR_test)
