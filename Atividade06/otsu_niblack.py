from skimage.filters.thresholding import threshold_otsu
from skimage.filters.thresholding import threshold_niblack
#from skimage.filters import (threshold_otsu, threshold_niblack, threshold_sauvola)

def otsu(imagem):
    limiar = threshold_otsu(imagem)
    return imagem > limiar

def niblack(imagem, ws=15, k=0.8):
    limiar = threshold_niblack(imagem, window_size=ws, k=k)
    return imagem > limiar