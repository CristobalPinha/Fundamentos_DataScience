import pandas as pd
from Leer_Limpiar import df

#I. Crear nueva columna "Poder Total" que sea la suma de ataque, defensa, velocidad y PS
df['Poder Total'] = df['Ataque'] + df['Defensa'] + df['Velocidad'] + df['PS']

print(f"\nSe ha creado la columna 'Poder Total'")
print(f"Promedio de Poder Total: {df['Poder Total'].mean().round(1)}")
print(f"Maximo Poder Total: {df['Poder Total'].max()}")
print(f"Minimo Poder Total: {df['Poder Total'].min()}")

#II. Ordenar el DataFrame por "Poder Total" de mayor a menor
df_Ordenado = df.sort_values(by='Poder Total', ascending=False)

print(f"\nDataFrame ordenado por Poder Total (de mayor a menor):")
print(f"Top 10 Pokemon con mayor Poder Total:\n")
print(df_Ordenado[['Nombre', 'Tipo 1', 'Tipo 2', 'Ataque', 'Defensa', 'Velocidad', 'PS', 'Poder Total']].head(10))

print(f"\nTop 5 Pokemon con menor Poder Total:\n")
print(df_Ordenado[['Nombre', 'Tipo 1', 'Tipo 2', 'Ataque', 'Defensa', 'Velocidad', 'PS', 'Poder Total']].tail(5))

#III. Pokemon con mayor y menor poder total
Mayor_Poder = df_Ordenado.iloc[0]
print(f"\nEl Pokemon con mayor poder total es:")
print(f"Nombre: {Mayor_Poder['Nombre']}")
print(f"Tipo 1: {Mayor_Poder['Tipo 1']}")
print(f"Poder Total: {Mayor_Poder['Poder Total']}")

Menor_Poder = df_Ordenado.iloc[-1]
print(f"\nEl Pokemon con menor poder total es:")
print(f"Nombre: {Menor_Poder['Nombre']}")
print(f"Tipo 1: {Menor_Poder['Tipo 1']}")
print(f"Poder Total: {Menor_Poder['Poder Total']}")