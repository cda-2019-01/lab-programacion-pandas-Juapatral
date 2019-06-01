##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

# leer archivo
import pandas as pd
archivo2 = pd.read_csv("tbl2.tsv",sep="\t")
archivo0 = pd.read_csv("tbl0.tsv",sep="\t")

# juntar archivos
archivom = archivo0.merge(archivo2,how='left',on='_c0')

# agregar
resul = archivom.groupby('_c5a').sum()['_c5b']

# imprimir
print(resul)
