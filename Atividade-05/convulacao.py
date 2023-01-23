# Imagem, Pixel[I][J], Janela = MxN, Type = Gray(-1) Red(0) Green (1) Blue(2)
def JanelaReplicada(Imagem,I,J,M,N,T):
    if T == -1:
        Altura, Largura = Imagem.shape
    else:
        Altura, Largura, _ = Imagem.shape
    janela = []    
    a = int((M-1)/2)
    b = int((N-1)/2)
    new_a = a*(-1)
    new_b = b*(-1)   
    for x in range(M):
        b = new_b
        for y in range(N):
            i_atual = I+new_a
            j_atual = J+b   
            if i_atual < 0: i_atual = 0
            elif i_atual >= Altura: i_atual = Altura-1
            if j_atual < 0: j_atual = 0
            elif j_atual >= Largura: j_atual = Largura-1
            if T == -1: janela.append(Imagem[i_atual][j_atual])
            else: janela.append(Imagem[i_atual][j_atual][T])
            b += 1
        new_a += 1        
    return janela

# Imagem, Pixel[I][J], Janela = MxN, Type = Gray(-1) Red(0) Green (1) Blue(2)
def JanelaEspelhada(Imagem,I,J,M,N,T):
    if T == -1:
        Altura, Largura = Imagem.shape
    else:
        Altura, Largura, _ = Imagem.shape
    janela = []    
    a = int((M-1)/2)
    b = int((N-1)/2)
    new_a = a*(-1)
    new_b = b*(-1)   
    for x in range(M):
        b = new_b
        for y in range(N):
            i_atual = I+new_a
            j_atual = J+b   
            if i_atual < 0: i_atual = Altura+i_atual
            elif i_atual >= Altura: i_atual = i_atual-Altura
            if j_atual < 0: j_atual = Largura+j_atual
            elif j_atual >= Largura: j_atual = j_atual-Largura
            if T == -1: janela.append(Imagem[i_atual][j_atual])
            else: janela.append(Imagem[i_atual][j_atual][T])
            b += 1
        new_a += 1        
    return janela

#
def imagemRGB(imagem,M,N,borda='ignore'):
    altura, largura, dime = imagem.shape
    resultados = []
    if borda == 'espelho':
        for I in range(altura):
            for J in range(largura):
                Lista = []
                Lista.append(JanelaEspelhada(Imagem,I,J,M,N,0))
                Lista.append(JanelaEspelhada(Imagem,I,J,M,N,1))
                Lista.append(JanelaEspelhada(Imagem,I,J,M,N,2))
                resultados.append(Lista)
    if borda == 'replicar':
        for I in range(altura):
            for J in range(largura):
                Lista = []
                Lista.append(JanelaReplicada(Imagem,I,J,M,N,0))
                Lista.append(JanelaReplicada(Imagem,I,J,M,N,1))
                Lista.append(JanelaReplicada(Imagem,I,J,M,N,2))
                resultados.append(Lista)


# Janela
def janela(imagem, filtro, borda,  l, a, largura, altura):
    janela = []
    for i in range(l-1, l+2): # tem que ajeitar isso aqui de acordo com o tamanho do kernel passado na variavel filtro
        for j in range(a-1, a+2): # tem que ajeitar isso aqui de acordo com o tamanho do kernel passado na variavel filtro
            if (i > -1 and j > -1) and (i < largura and j < altura):
                janela.append(imagem[i][j])
            elif borda == 'padding': # Se a borda for padding, preenche os valores fora da imagem com 0
                janela.append(0)
            '''
            elif borda == 'espelho': # Se a borda for espelho, preenche os valores fora da imagem com o valor do pixel mais próximo.
                pass
            elif borda == 'replicar': # Se a borda for replicar, preenche os valores fora da imagem com o valor da borda mesmo.
                pass
            '''
    return janela

def convColorida(imagem, filtro, borda):
	
    pass

def convCinza(imagem, filtro, borda):
	altura, largura = imagem.shape
	resultados = []
	if borda == 'replicar':
		for I in range(altura):
			for J in range(largura):
				resultados.append(JanelaReplicada(imagem,I,J,filtro['M'],filtro['N'],-1))
	elif borda == 'espelho':
		for I in range(altura):
			for J in range(largura):
				resultados.append(JanelaEspelhada(imagem,I,J,filtro['M'],filtro['N'],-1))
	else:
		for I in range(altura):
			for J in range(largura):
				resultados.append(janela(imagem,filtro,borda,I,J,largura,altura)

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
