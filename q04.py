##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 


# leer archivo
import pandas as pd
archivo = pd.read_csv("tbl1.tsv",sep="\t")

# agrupar
resul = list(set(archivo["_c4"]))

# convertir a mayusculas y ordenar
resul2 = [letra.upper() for letra in resul]
resul2.sort()

# imprimir
print(resul2)