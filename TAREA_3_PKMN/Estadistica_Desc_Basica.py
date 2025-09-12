import pandas as pd
from Leer_Limpiar import df

#I. Promedio, mediana y moda del ataque de todos los pokemones
Promedio_Ataque = df['Ataque'].mean().round(1)
print(f"\nEl promedio de ataque es: {Promedio_Ataque}")

Mediana_Ataque = df['Ataque'].median()
print(f"\nLa mediana de ataque es: {Mediana_Ataque}")

Moda_Ataque = df['Ataque'].mode()
print(f"\nLa moda de ataque es: {Moda_Ataque[0]} Se repite: {len(Moda_Ataque)} veces")


#II. Pokemon con mayor defensa y menor velocidad
Mayor_Defensa = df[df['Defensa'] == df['Defensa'].max()]
print(f"\nEl Pokemon con mayor defensa es:\n")
print(Mayor_Defensa[['Nombre', 'Tipo 1', 'Tipo 2', 'Ataque', 'Defensa', 'Velocidad', 'PS']])

Menor_Velocidad = df[df['Velocidad'] == df['Velocidad'].min()]
print(f"\nEl Pokemon con menor velocidad es:\n")
print(Menor_Velocidad[['Nombre', 'Tipo 1', 'Tipo 2', 'Ataque', 'Defensa', 'Velocidad', 'PS']])

#III. Pokemones con dos tipos validos
Dos_Tipos = df[df['Tipo 2'].notnull()]
print(f"\nPokemones con dos tipos validos de primera generacion: {len(Dos_Tipos)}")

#IV. Rango y desviacion estandar de los PS de cada pokemon
Rango_PS = df['PS'].max() - df['PS'].min()
print(f"\nEl rango de los PS de todos los pokemones es:{Rango_PS}")

Desviacion_estandar_PS = df['PS'].std().round(1)
print(f"\nLa desviacion estandar de los PS es: {Desviacion_estandar_PS}")
