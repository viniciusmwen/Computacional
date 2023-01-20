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
        self.altura = 240
        self.largura = 240
        self.dimensoes = None
    
    # Ler a imagem, imagem redimensionada e imagem em tons de cinza.
    def ler(self):
        self.img = imread(self.name)
        self.imgRed = resize(self.img, (self.largura, self.altura))
        self.imgGray = rgb2gray(self.imgRed)

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
    
    def show(self, img=None, title=""):
        
        if img is None:
            image = self.img
        else:
            image = img

        plt.imshow(image, cmap='gray')
        plt.title(f'{title}\n{image.shape}')
        plt.axis('off')

    # Função que apresenta várias imagens.
    def manyShow(self, *imgs, color=None):
        _, ax = plt.subplots(1, len(imgs), figsize=(20, 20),sharex=True)
        for index, i in enumerate(ax):
            i.imshow(imgs[index], cmap=color)
            i.set_title(f'{imgs[index].shape}')
            i.axis('off')

    # Função que apresenta várias imagens com títulos.
    def manyShowWithTitle(self, *imgs, color=None):
        _, ax = plt.subplots(1, len(imgs), figsize=(20, 20),sharex=True)
        for index, i in enumerate(ax):
            i.imshow(imgs[index]['img'], cmap=color)
            i.set_title(f'{imgs[index]["title"]} \n {imgs[index]["img"].shape}')
            i.axis('off')




