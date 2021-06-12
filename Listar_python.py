## first install conda install -c conda-forge xlsxwriter and conda install -c anaconda openpyxl
from os import listdir
from os.path import isfile, join
import pandas as pd


def ls(ruta = '/Users/andresmauriciotrianareina/Downloads/Actas de entrega participantes'):
    ls.para = [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]
    #print(ls.para)

    df = pd.DataFrame(ls.para, columns=['cedulas'])

    print(df['cedulas'])
    
    df.to_excel('cedulas.xlsx', sheet_name='cedulas')

print(ls())