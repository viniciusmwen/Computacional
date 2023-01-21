import numpy as np
from tqdm import tqdm

def janela(img, l, a, largura, altura):
    janela = []
    for i in range(l-1, l+2): # tem que ajeitar isso aqui de acordo com o tamanho do kernel passado na variavel filtro
        for j in range(a-1, a+2): # tem que ajeitar isso aqui de acordo com o tamanho do kernel passado na variavel filtro
            if (i > -1 and j > -1) and (i < largura and j < altura):
                janela.append(img[i][j])
            elif borda == 'padding':
                janela.append(0)
            elif borda == 'espelho':
                pass
            elif borda == 'replicar':
                pass
    return janela

def padding(img):
    largura, altura = img.shape
    img2 = img
    for l in tqdm(range(largura)):
        for a in range(altura):
            janela = janela(img2, l, a, largura, altura)
            img2[l][a] = np.sum(janela) / len(janela)
    return img2
