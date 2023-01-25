## Fazer as funções de aplicar filtros não lineares: mediana, moda, maximo e minimo
## Em uma imagem onde o tamanho do quadro (kernel) é repassado
## Como parâmetro. O tamanho do quadro deve ser ímpar.

import cv2
import numpy as np
import matplotlib.pyplot as plt
import statistics
import pandas as pd
from tqdm import tqdm

def mediana(img, kernel):
    # retorna a mediana dos valores que estão no kernel
    # Aplicar filtro mediana
    #resultado = pd.DataFrame(kernel).median()
    """ if kernel[0] > 0 and kernel[0] < 1.0:
        resultado = pd.DataFrame(kernel).median()
    else:
        resultado = statistics.median(kernel) """
    resultado = np.median(kernel)
    return resultado

def moda(img, kernel):
    # Aplicar filtro moda
    resultado = statistics.mode(kernel)
    return resultado

def maximo(img, kernel):
    # Aplicar filtro maximo
    #resultado = pd.DataFrame(kernel).max()[0]
    resultado = max(kernel)
    return resultado

def minimo(img, kernel):
    # Aplicar filtro minimo
    #resultado = pd.DataFrame(kernel).min()[0]
    resultado = min(kernel)
    return resultado

def montaJanela(img, t1, t2, i, j):
    # Montar janela
    janela = []
    cont = 0
    for l in range(i-(t1//2), i+(t2//2)+1):
        for c in range(j-(t1//2), j+(t2//2)+1):
            if l > 0 and l < img.shape[0]-1 and c > 0 and c < img.shape[1]-1:
                #janela[cont] = img[l,c]
                janela.append(img[l,c])
    return janela

def escolheFiltro(img, filtro, kernel, i, j):
    resultado = None
    janela = montaJanela(img, int(kernel[0]), int(kernel[1]), i, j)

    if filtro == 'mediana':
        resultado = mediana(img, janela)
    elif filtro == 'moda':
        resultado = moda(img, janela)
    elif filtro == 'maximo':
        resultado = maximo(img, janela)
    elif filtro == 'minimo':
        resultado = minimo(img, janela)

    return resultado


def applyColor(img, filtro, kernel):
    # Aplicar filtro
    if img.dtype == np.uint8:
        imgFiltrada = np.zeros(img.shape, dtype=np.uint8)
    else:
        imgFiltrada = img.copy().astype(np.float32)

    for i in tqdm(range(1, img.shape[0]-1), desc=f"{filtro} - {kernel}"):
        for j in range(1, img.shape[1]-1):
            for k in range(3):
                imgFiltrada[i,j,k] = escolheFiltro(img[:,:,k], filtro, kernel, i, j)

    return imgFiltrada


# function to apply the filter solved the problem: "setting an array element with a sequence".
def applyFilter(img, filtro, kernel):
    # Aplicar filtro
    if img.dtype == np.uint8:
        imgFiltrada = np.zeros(img.shape, dtype=np.uint8)
    else:
        imgFiltrada = img.copy().astype(np.float32)

    if len(img.shape) < 3:
        for i in tqdm(range(1, img.shape[0]-1), desc=f"{filtro} - {kernel}"):
            for j in range(1, img.shape[1]-1):
                imgFiltrada[i,j] = escolheFiltro(img.astype(np.float32), filtro, kernel, i, j)
    else:
        imgFiltrada = applyColor(img, filtro, kernel)

    return imgFiltrada

