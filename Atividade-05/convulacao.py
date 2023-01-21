
def janela(imagem, filtro, borda,  l, a, largura, altura):
    janela = []
    for i in range(l-1, l+2): # tem que ajeitar isso aqui de acordo com o tamanho do kernel passado na variavel filtro
        for j in range(a-1, a+2): # tem que ajeitar isso aqui de acordo com o tamanho do kernel passado na variavel filtro
            if (i > -1 and j > -1) and (i < largura and j < altura):
                janela.append(imagem[i][j])
            elif borda == 'padding': # Se a borda for padding, preenche os valores fora da imagem com 0
                janela.append(0)
            elif borda == 'espelho': # Se a borda for espelho, preenche os valores fora da imagem com o valor do pixel mais próximo.
                pass
            elif borda == 'replicar': # Se a borda for replicar, preenche os valores fora da imagem com o valor da borda mesmo.
                pass
    return janela

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


""" 
    filtro seria um dicionario com dois valores: {
        'M': 3,
        'N': 3,
    }, tem as condições lá na atividade.

    borda seria uma string com os valores: 'ignore', 'padding', 'espelho', 'replicar'
"""