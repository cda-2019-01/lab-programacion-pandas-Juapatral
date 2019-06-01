##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

# leer archivo
import pandas as pd
archivo = pd.read_csv("tbl0.tsv",sep="\t")

# crear columna
archivo['suma'] = archivo['_c0'] + archivo['_c2']

print(archivo)
