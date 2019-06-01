##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

# leer archivo
import pandas as pd
archivo = pd.read_csv("tbl1.tsv",sep="\t")

# agrupar archivo
archivo2=archivo.groupby("_c0")['_c4']

# mostrar datos
data = [] 
for key, item in archivo2:
    data.append(list(archivo2.get_group(key)))

# ordenarlos
for a in data:
    a.sort()

# juntarlos con dos puntos
data = [",".join(a) for a in data]

# juntar dataframes
resul3 = pd.DataFrame({'_c0':list(archivo2.groups.keys()),'lista':data})

# imprimir
print(resul3)