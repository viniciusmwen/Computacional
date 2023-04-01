import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from skimage.io import imread,imsave,imshow
from skimage.color import rgb2gray
import cv2
import os
import csv
from tqdm import tqdm
from skimage.transform import resize
import seaborn as sns
from skimage.exposure import equalize_hist
from skimage.filters.thresholding import threshold_otsu
from skimage.filters import median

class Imagem():

    def __init__(self, name='sunflower.jpg'):
        self.name = name
        self.img = None
        self.imgGray = None
        self.imgRed = None
        self.dimensoes = None
        self.altura = 240
        self.largura = 240
        self.dimensoes = None
        self.filtros = {}
        self.imgs = []
        self.img_redimensionadapt = None # Imagem redimensionada
    
    # Ler a imagem, imagem redimensionada e imagem em tons de cinza.
    def ler(self):
        # Ler a imagem como um array flutuante
        self.img = imread(self.name)
        self.imgRed = resize(self.img, (self.largura, self.altura))
        
        if len(self.imgRed.shape) == 3:
            self.imgGray = rgb2gray(self.imgRed)

            self.dimensoes = {
                0: self.imgRed[:,:,0],
                1: self.imgRed[:,:,1],
                2: self.imgRed[:,:,2]
            }
        else:
            self.dimensoes = {0: self.img}
    
    # Ler a imagem, imagem redimensionada e imagem em tons de cinza.
    def lerCV2(self):
        # Ler a imagem como um array inteiro
        self.img = cv2.imread(self.name)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB) 
        self.imgRed = cv2.resize(self.img, (240, 240))
        
        if len(self.imgRed.shape) == 3:
            self.imgGray = cv2.cvtColor(self.imgRed, cv2.COLOR_RGB2GRAY)
            self.dimensoes = {
                0: self.imgRed[:,:,0],
                1: self.imgRed[:,:,1],
                2: self.imgRed[:,:,2]
            }
        else:
            self.dimensoes = {0: self.img}

    # Função que apresenta as imagens.
    def shows(self, modo=0):
        if modo == 0:
            self.show(self.img)
        elif modo == 1:
            self.manyShowWithTitle(
                {'img': self.img, 'title': f'Tamanho original'},
                {'img': self.imgRed, 'title': f'Tamanho padronizado'},
                color='gray')
        elif modo == 2:
            self.manyShowWithTitle(
                {'img': self.img, 'title': f'Tamanho original'},
                {'img': self.imgGray, 'title': f'Preto e Branco'},
                color='gray')

        elif modo == 3:
            self.manyShowWithTitle(
                {'img': self.img, 'title': f'Tamanho original'},
                {'img': self.imgRed, 'title': f'Tamanho padronizado'},
                {'img': self.imgGray, 'title': f'Preto e Branco'},
                color='gray')
        
        elif modo == 4:
            self.manyShowWithTitle(
                {'img': self.imgRed, 'title': f'OriginalTamanho padronizado'},
                {'img': self.dimensoes[0], 'title': f'Canal Vermelho'},
                {'img': self.dimensoes[1], 'title': f'Canal Verde'},
                {'img': self.dimensoes[2], 'title': f'Canal Azul'},
                color='gray')
        
        elif modo == 5:
            self.manyShowWithTitle(
                {'img': self.imgRed, 'title': f'Original'},
                {'img': self.filtros['eq'], 'title': f'Equalizada'},
                {'img': self.filtros['median'], 'title': f'Median'},
                {'img': self.dimensoes[0], 'title': f'Canal Vermelho'},
                {'img': self.dimensoes[1], 'title': f'Canal Verde'},
                {'img': self.dimensoes[2], 'title': f'Canal Azul'},
                color='gray')
        
    # Função que apresenta uma imagem.
    def show(self, img=None, title=""):
        
        if img is None:
            image = self.img
        else:
            image = img

        plt.imshow(image, cmap='gray')
        plt.title(f'{title}\n{image.shape}')
        plt.axis('off')

    def defineLinhasColunas(self, imgs, linhas, colunas):
        if linhas == None or colunas == None:
            print(len(imgs))
            if len(imgs) > 4:
                colunas = 4
                linhas = len(imgs)//4+1
            else:
                colunas = len(imgs)
                linhas = 1
        
        return linhas, colunas

    # Função que apresenta várias imagens.
    def manyShow(self, *imgs, color='gray'):
        _, ax = plt.subplots(1, len(imgs), figsize=(20, 20),sharex=True)
        for index, i in enumerate(ax):
            i.imshow(imgs[index], cmap=color)
            i.set_title(f'{imgs[index].shape}')
            i.axis('off')

    # Função que apresenta várias imagens com títulos.
    def manyShowWithTitle(self, *imgs, color='gray'):
        _, ax = plt.subplots(1, len(imgs), figsize=(20, 20), sharex=True)
        for index, i in enumerate(ax):
            i.imshow(imgs[index]['img'], cmap=color)
            i.set_title(f'{imgs[index]["title"]} \n {imgs[index]["img"].shape}')
            i.axis('off')

    def redimensionar(self, porcentagem=0.8):
        altura, largura = self.dimensoes[0].shape
        novaAltura, novaLargura = int(altura*porcentagem), int(largura*porcentagem)
        self.img_redimensionada = resize(self.dimensoes[0], (novaAltura,novaLargura), anti_aliasing=True)

    def abrirVarios(self, *caminhos):
        for caminho in caminhos:
            self.imgs.append(imread(caminho))
    
    def mostraIMGS(self, title=None):
        if len(title) != len(self.imgs):
            print('Quantidade de titulos diferente da quantidade de imagens.')
            return
        r = []
        for i in range(len(self.imgs)):
            r.append({'img': self.imgs[i], 'title': title[i]})
        self.manyShowWithTitle(*r)
    
    def scatterMostra(matriz, xlabel, ylabel, color='red'):
        sns.scatterplot(x=matriz[xlabel], y=matriz[ylabel], hue=matriz['className'])
        plt.title(f'{xlabel} x {ylabel}')
        plt.show()

    def equalize(self, img=None):

        if img == None:
            img = self.imgRed

        img_eq = np.zeros_like(img)
        for d in range(img.shape[2]):
            img_eq[:,:,d] = equalize_hist(img[:,:,d])
        return img_eq

    def normalize(self, imagem=None):
        if imagem == None:
            imagem = self.imgRed

        copia = imagem.copy()
        copia = copia / 255
        copia = copia[:,:,0] + copia[:,:,1] + copia[:,:,2]

        return copia

        

    def otsu(self, imagem=None):

        if imagem == None:
            imagem = self.normalize(self.filtros['median'])
        
        limiar = threshold_otsu(imagem)
        return imagem > limiar

    def inteiro(self, imagem=None):
        if imagem == None:
            imagem = self.imgRed

        copia = imagem.copy()
        copia = copia * 255
        copia = copia.astype(np.uint8)

        return copia

    def salvar(self, imgs, originais, caminho):
        for i, img in enumerate(imgs):
            nome = originais[i].split('/')[-2] + '/' + originais[i].split('/')[-1]
            #imsave(f'{caminho}/{nome}', img)
            plt.imsave(f'{caminho}/{nome}', img)
            