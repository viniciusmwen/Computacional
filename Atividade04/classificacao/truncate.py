import pandas as pd
import csv

# função que converte valores para 3 casas decimais de um dataset
def truncate(df):
    #print(df.head())
    f = ['mlp', 'randomForest', 'svm','xbr']
    for i in f:
        for j in df[i]:
            df[i] = df[i].apply(lambda x: round(x, 3))
    return df

def LinhaCSV(Dados, Arquivo):
    # Ordem: NomeArquivo,Largura, Altura, Média,
    # Variância, Skewness,Kurtosis, Energy, Entropy, NomeClasse, ClasseId
    with open(Arquivo,'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(Dados)



df = truncate(pd.read_csv('negativo.csv'))
LinhaCSV(df.columns, 'negativo2.csv')
for i in df.values:
    LinhaCSV(i, 'negativo2.csv')

print(df.head())