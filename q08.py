##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

# leer archivo
import pandas as pd
archivo = pd.read_csv("tbl0.tsv",sep="\t")

# crear columna
archivo['ano'] = [x[0] for x in archivo['_c3'].str.split("-")]

# imprimir
print(archivo)
