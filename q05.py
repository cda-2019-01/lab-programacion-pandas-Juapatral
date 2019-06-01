##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

# leer archivo
import pandas as pd
archivo = pd.read_csv("tbl0.tsv",sep="\t")

# agrupar
resul=archivo.groupby("_c1").sum()

# imprimir
print(resul["_c2"])