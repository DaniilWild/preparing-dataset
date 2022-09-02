import os
import numpy as np
import cv2
import hashlib

def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0.1
      var = 0.11
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss

      return noisy


PATH = "/content/test"
PATH_dd = "/content/test_new/"


print("Все папки и файлы:", os.listdir(PATH))

images = os.listdir(PATH)

for image in images:
  img = cv2.imread(os.path.join(PATH , image))
  img = noisy("gauss",img)
  cv2.imwrite(os.path.join(PATH_dd , image),img)
