import pandas as pd
from Leer_Limpiar import df

#Selecciono solo los pokemones tipo fuego, y 4 columnas
Tipo_Fuego = df[df['Tipo 1'] == 'Fuego']
Columnas_Seleccionadas = Tipo_Fuego[['Nombre', 'Tipo 1', 'Ataque', 'Velocidad']]

#Imprimir los pokemones tipo fuego, cuantos son y la lista
print(f'Los Pokemones tipo fuego son: {len(Tipo_Fuego)}\n')
print(Columnas_Seleccionadas)
