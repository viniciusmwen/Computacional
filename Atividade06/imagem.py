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
        self.img_redimensionadapt = None # Imagem redimensionada
    
    # Ler a imagem, imagem redimensionada e imagem em tons de cinza.
    def ler(self):
        # Ler a imagem como um array flutuante
        self.img = imread(self.name)
        self.imgRed = resize(self.img, (self.largura, self.altura))
        
        if len(self.imgRed.shape) == 3:
            self.imgGray = rgb2gray(self.imgRed)

            self.dimensoes = {
                0: self.img[:,:,0],
                1: self.img[:,:,1],
                2: self.img[:,:,2]
            }
        else:
            self.dimensoes = {0: self.img}
    
    # Ler a imagem, imagem redimensionada e imagem em tons de cinza.
    def lerCV2(self):
        # Ler a imagem como um array inteiro
        self.img = cv2.imread(self.name)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB) 
        self.imgRed = cv2.resize(self.img, (240, 240))
        self.imgGray = cv2.cvtColor(self.imgRed, cv2.COLOR_RGB2GRAY)

    # Função que apresenta as imagens.
    def shows(self, qnt=2):
        if qnt == 0:
            self.show(self.img)
        elif qnt == 1:
            self.manyShowWithTitle(
                {'img': self.img, 'title': f'Tamanho original'},
                {'img': self.imgRed, 'title': f'Tamanho padronizado'},
                color='gray')
        elif qnt == 2:
            self.manyShowWithTitle(
                {'img': self.img, 'title': f'Tamanho original'},
                {'img': self.imgRed, 'title': f'Tamanho padronizado'},
                {'img': self.imgGray, 'title': f'Preto e Branco'},
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

    # Função que apresenta várias imagens.
    def manyShow(self, *imgs, color='gray'):
        _, ax = plt.subplots(1, len(imgs), figsize=(20, 20),sharex=True)
        for index, i in enumerate(ax):
            i.imshow(imgs[index], cmap=color)
            i.set_title(f'{imgs[index].shape}')
            i.axis('off')

    # Função que apresenta várias imagens com títulos.
    def manyShowWithTitle(self, *imgs, color='gray'):
        _, ax = plt.subplots(1, len(imgs), figsize=(20, 20),sharex=True)
        for index, i in enumerate(ax):
            i.imshow(imgs[index]['img'], cmap=color)
            i.set_title(f'{imgs[index]["title"]} \n {imgs[index]["img"].shape}')
            i.axis('off')

    def redimensionar(self, porcentagem=0.8):
        altura, largura = self.dimensoes[0].shape
        novaAltura, novaLargura = int(altura*porcentagem), int(largura*porcentagem)
        self.img_redimensionada = resize(self.dimensoes[0], (novaAltura,novaLargura), anti_aliasing=True)



