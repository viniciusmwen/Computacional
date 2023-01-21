import numpy as np
from tqdm import tqdm

def janela(img, l, a, largura, altura):
    janela = []
    for i in range(l-1, l+2):
        for j in range(a-1, a+2):
            if (i > -1 and j > -1) and (i < largura and j < altura):
                janela.append(img[i][j])
            else:
                janela.append(0)
    return janela

def padding(img):
    largura, altura = img.shape
    img2 = img
    for l in tqdm(range(largura)):
        for a in range(altura):
            janela = janela(img2, l, a, largura, altura)
            img2[l][a] = np.sum(janela) / len(janela)
    return img2
