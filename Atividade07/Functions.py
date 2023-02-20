import pandas as pd
import numpy as np
from skimage.io import imread, imsave, imshow
from skimage.color import rgb2gray
import cv2
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage.filters.thresholding import threshold_otsu
import glob

# Função para obter os caminhos de arquivos de uma pasta específica.
def caminhos_dataset(base='./Imagens/DSFlowersV1/'):
    resultados = []
    for diretorio, subpastas, arquivos in os.walk(base):
        for arquivo in arquivos:
            resultados.append(os.path.join(diretorio,arquivo))
    return resultados

# Função para ler um imagem em níveis de cinza.
def leitura_cinza(imagem:str):
    # imagemCinza = cv2.imread(imagem,0)
    imagemCinza = imread(imagem,as_gray=True)
    return imagemCinza

# Função para exibir uma imagem.
def show(img):
    plt.imshow(img,cmap=plt.cm.binary,interpolation='nearest')
    plt.axis("off")
    plt.show()

# Função que retorna o histograma de uma imagem em níveis de cinza.
def histograma(imagem):
    linhas, colunas = imagem.shape
    valores = []
    # Inicializando os resultados.
    for i in range(256):
        valores.append(0)
    # Percorrendo a imagem.
    for l in range(linhas):
        for c in range(colunas):
            valores[int(imagem[l][c])] += 1
    return valores

# Função do Alargamento de Contraste.
def alargamentoDeContraste(r,k,E):
    return 1/(1+((k/r)**E))

# Função para aplicar o Alargamento de Contraste.
def aplicaAlargamento(imagem:str,k:int,E:float):
    imagemCinza = leitura_cinza(imagem)
    novaImagem = imagemCinza.copy()
    linhas, colunas =  imagemCinza.shape
    for l in range(linhas):
        for c in range(colunas):
            pixel = novaImagem[l][c]
            novaImagem[l][c] = alargamentoDeContraste(pixel,k,E)
    # plt.imsave('Alargamento-03.png',novaImagem,cmap=plt.cm.gray)
    return novaImagem

# Função para aplicar o K-Means.
def aplicaKMeans(imagem):
    # imagemCinza = leitura_cinza(imagem)
    kmeans = KMeans(n_clusters=2,n_init='auto')
    imagemTreinamento = np.reshape(imagem,(-1,1))
    kmeans.fit(imagemTreinamento)
    resultado = (kmeans.labels_.reshape(imagem.shape))
    return resultado
    # plt.imsave('KMeans-03.png',resultado,cmap=plt.cm.gray)

# Função para aplicar Otsu.
def aplicaOtsu(imagem):
    limiar = threshold_otsu(imagem)
    return imagem > limiar

# Função para criar uma pasta.
def montaPasta(tipo,nome):
    pasta = ''
    for i in nome:
        if i != '/':
            pasta += i
        else:
            pasta += i
            break
    nomeFlower = nome.replace(pasta,"")
    
    nomeFlower = nomeFlower.replace(" ","")
    # print(nomeFlower)
    dir = './resultados/'+tipo+'/'+pasta
    # print( dir,nomeFlower)
    return dir,nomeFlower

def pegaData(c):
    return sorted(glob(f'{c}/*', recursive=True))

# Alargamento-01.png com k=10 e E=1.0
# Alargamento-02.png com k=30 e E=2.0
# Alargamento-03.png com k=30 e E=3.0
# KMeans-01.png com 2 Clusters
# KMeans-02.png com 3 Clusters
# KMeans-03.png com 8 Clusters
# imagemCinza = leitura_cinza('MimeJr.png')
# print(histograma(imagemCinza))
# caminhos_dataset()
# aplicaKMeans('MimeJr.png')
# montaPasta('alargamento71','daisy/daisy-089.jpg')