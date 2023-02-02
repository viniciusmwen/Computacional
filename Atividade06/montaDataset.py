from glob import glob

def pegaData(caminho):
    return glob(f'{caminho}/*', recursive=True)



