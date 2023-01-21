
def janela(imagem, filtro, borda,  l, a, largura, altura):
    pass

def convColorida(imagem, filtro, borda):
    pass

def convCinza(imagem, filtro, borda):
    pass

def verificaFiltro(filtro, imagem):
    r = False
    if (filtro['M'] % 2 != 0) and (filtro['N'] % 2 != 0) and (filtro['M'] >= 3) and (filtro['N'] >= 3) and (filtro['M'] < imagem.shape[0]) and (filtro['N'] < imagem.shape[1]):
        r = True
    return r

def convulacao(imagem, filtro, borda='ignore'):

    if verificaFiltro(filtro, imagem):
        if len(imagem.shape) == 3:
            imagem_processada = convColorida(imagem, filtro, borda)
        else:
            imagem_processada = convCinza(imagem, filtro, borda)
    else:
        print('Erro: O filtro não é compatível com a imagem.')
        imagem_processada = None

    return imagem_processada
