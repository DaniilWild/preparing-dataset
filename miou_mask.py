try:
    import os
    import cv2
    import numpy as np
    import math
    import warnings
    warnings.filterwarnings("ignore", category=RuntimeWarning)
except ModuleNotFoundError:
    assert False, "Не найден нужный модуль"


def compute_miou(actual, pred):
    num_class = 21

    actual = cv2.imread(actual)
    pred = cv2.imread(pred)

    a = actual
    a = a.reshape((a.size,))
    a_count = np.bincount(a, weights = None, minlength = num_class) # A

    b = np.resize(pred, (actual.shape[0] ,actual.shape[1], 3))
    b = b.reshape((b.size,))
    b_count = np.bincount(b, weights=None, minlength=num_class)  # B

    c = a * num_class + b
    cm = np.bincount(c, weights=None, minlength=num_class * num_class)
    cm = cm.reshape((num_class, num_class))

    Nr = np.diag(cm)  # A ⋂ B
    Dr = a_count + b_count - Nr  # A ⋃ B
    individual_iou = Nr / Dr
    miou = np.nanmean(individual_iou)
    return miou

if __name__ == '__main__':

    mask_true_dir = "/content/train_masks/"  # путь к mask_private или mask_public
    mask_pred_dir = "/content/train_masks/"   # путь к маскам участника

    try:
        mask_true = []
        for _, _, files in os.walk(mask_true_dir):
            for x in files:
                if x.endswith(".png") == True:
                    mask_true.append(x)
    except Exception:
        assert False, 'Ошибка при загрузке эталонного решения'

    try:
        mask_pred = []
        for _, _, files in os.walk(mask_pred_dir):
            for y in files:
                if y.endswith(".png") == True:
                    mask_pred.append(y)
    except Exception:
        assert False, 'Ошибка при загрузке решения участника'

    assert not(len(mask_pred) == 0), 'Ошибка при загрузке решения участника'
    assert not (len(mask_true) == 0), 'Ошибка при загрузке эталонного решения'

    try:
        score = 0
        for mask in mask_true:
          score += compute_miou(mask_true_dir + mask, mask_pred_dir + mask)
    except Exception:
        assert False, 'Некорректные наименования файлов'

    if math.isnan(score):
        assert False, 'Некорректные наименования файлов'
    score /= len(mask_true)

