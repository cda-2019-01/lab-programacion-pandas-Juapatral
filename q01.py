##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 

# leer archivo
import pandas as pd
archivo = pd.read_csv("tbl0.tsv",sep="\t")

# agrupar
resul=archivo.groupby("_c1").count()

# imprimir
print(resul["_c0"])