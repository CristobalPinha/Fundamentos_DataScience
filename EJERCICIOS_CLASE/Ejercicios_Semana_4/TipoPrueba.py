import numpy as np
import pandas as pd

#Dado un dataframe con mediciones de sensor con valores nulos, identifiquen las filas que contienen  valores nulos y creen una nueva sin estas filas y otras rellenando los nulos con la media o el valor anterior

datos = {'Tiempo (s)': [0, 1, 2, 3, 4, 5],
         'Temp (°C)': [22.1, 22.3, np.nan, 22.8, 22.5, np.nan],
         'Humedad (%)': [45, 46, 45, np.nan, 48, 47]}

df = pd.DataFrame(datos)

# Identificar filas con valores nulos
filas_nulas = df[df.isnull().any(axis=1)] #isnull() identifica los nulos, any(axis=1) verifica si hay algun nulo en la fila

# Crear nuevo DataFrame sin filas nulas
df_sin_nulos = df.dropna() #Dropna elimina las filas que contienen nulos

# Rellenar nulos con la media de la columna
df_rellenado_media = df.fillna(df.mean()) #fillna() rellena los nulos con el valor especificado, en este caso la media de cada columna

# Rellenar nulos con el valor anterior
df_rellenado_anterior = df.fillna(method='ffill') #ffill (forward fill) rellena los nulos con el valor anterior.

print("Filas con valores nulos:\n", filas_nulas)
print("\nDataFrame sin filas nulas:\n", df_sin_nulos)
print("\nDataFrame con nulos rellenados con la media:\n", df_rellenado_media)
print("\nDataFrame con nulos rellenados con el valor anterior:\n", df_rellenado_anterior)

