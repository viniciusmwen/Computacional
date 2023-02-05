import numpy as np #para manipular os vetores
from matplotlib import pyplot as plt #para plotar os gráficos
from sklearn.cluster import KMeans #para usar o KMeans
from imagem import Imagem
from skimage.filters.rank import mean
from skimage.filters.thresholding import threshold_otsu
from glob import glob




def aplicaKM(kmeans, imagem):
    img2 = np.reshape(imagem, (-1,1))
    kmeans.fit(img2)
    resultado = (kmeans.labels_.reshape(imagem.shape))
    return resultado
