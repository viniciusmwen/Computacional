from glob import glob

def pegaData(caminho):
    return sorted(glob(f'{caminho}/*', recursive=True))



