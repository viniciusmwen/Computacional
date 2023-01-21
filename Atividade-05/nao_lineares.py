import numpy as np
from tqdm import tqdm
import statistics
from scipy import stats as st
from collections import Counter

def janela_noLinear(img, l, a, largura, altura, m, n):
    janela = []
    for i in range(l-(m//2), l+(m//2)+1): 
        for j in range(a-(n//2), a+(n//2)+1):
            if (i > -1 and j > -1) and (i < largura and j < altura):
                janela.append(img[i][j])
    return janela

""" 
    a.Mediana
    b.Mode
    c.Máximo
    d.Mínimo
"""

def moda(janela):
    c = Counter(janela)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


def escolheFiltro(filtro, janela):
    if filtro == 'a':
        return np.median(janela)
    elif filtro == 'b':
        # calcule the mode
        return moda(janela)[0]
    elif filtro == 'c':
        return np.max(janela)
    elif filtro == 'd':
        return np.min(janela)

def aplica(img, m, n, filtro):
    largura, altura = img.shape
    img2 = img
    for l in tqdm(range(largura)):
        for a in range(altura):
            janela = janela_noLinear(img2, l, a, largura, altura, m, n)
            img2[l][a] = escolheFiltro(filtro, janela)
    return img2

def noLinear_colorido(img, m, n, filtro):
    img2 = img
    for c in range(3):
        img2[:,:,c] = aplica(img2[:,:,c], m, n, filtro)
    return img2

def nao_linear(img, m, n, filtro):
    img = img
    if len(img.shape) == 3:
        img2 = noLinear_colorido(img, m, n, filtro)
    else:
        img2 = aplica(img, m, n, filtro)
    return img2