try:
    import json
    import os
    import numpy as np
    import math
    import warnings
    warnings.filterwarnings("ignore", category=RuntimeWarning)
except ModuleNotFoundError:
    assert False, "Не найден нужный модуль"

def compute_metric(actual, pred, outImageW, outImageH):

  data_true = json.load(open(actual))
  data_pred = json.load(open(pred))

  x_center_true = int((data_true["left_top"][0] + data_true["right_bottom"][0])/2)
  y_center_true = int((data_true["left_top"][1] + data_true["right_bottom"][1])/2)

  x_metr = x_center_true - int((data_pred["left_top"][0] + data_pred["right_bottom"][0])/2)
  y_metr = y_center_true - int((data_pred["left_top"][1] + data_pred["right_bottom"][1])/2)

  metr =  1- 0.7 * (abs(x_metr)/outImageH + abs(y_metr)/outImageW)/2 + 0.3 *abs(data_true["angle"] - data_pred["angle"])/359
  return metr


if __name__ == '__main__':

    json_true_dir = ""  # путь к json_private или json_public
    json_pred_dir = ""  # путь к фалам участника

    outImageW = 4096    # размер фотографии подложки
    outImageH = 4096

    try:
        json_true = []
        for _, _, files in os.walk(json_true_dir):
            for x in files:
                if x.endswith(".json"):
                    json_true.append(x)
    except Exception:
        assert False, 'Ошибка при загрузке эталонного решения'

    try:
        json_pred = []
        for _, _, files in os.walk(json_pred_dir):
            for y in files:
                if y.endswith(".json"):
                    json_pred.append(y)
    except Exception:
        assert False, 'Ошибка при загрузке решения участника'

    assert not(len(json_pred) == 0), 'Ошибка при загрузке решения участника'
    assert not (len(json_true) == 0), 'Ошибка при загрузке эталонного решения'

    try:
        score = 0
        for json_f in json_true:
            score += compute_metric(json_true_dir + json_f, json_pred_dir + json_f, outImageW, outImageH)
    except Exception:
        assert False, 'Некорректные наименования файлов'

    if math.isnan(score):
        assert False, 'Некорректные наименования файлов'
    try:
        score = score / len(json_true)
    except Exception:
          assert False, 'В проверяемом файле отсутствуют столбцы для проверки'