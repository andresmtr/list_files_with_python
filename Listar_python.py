## the next imports 

from os import listdir
from os.path import isfile, join
import pandas as pd

## include path of file to list

def ls(ruta = 'c://documents'):
    ls.para = [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]
    #print(ls.para)

    df = pd.DataFrame(ls.para, columns=['name_column'])

    print(df['name_column'])
    
    ## create excel with the information

    df.to_excel('name_excel.xlsx', sheet_name='name_sheet')

print(ls())