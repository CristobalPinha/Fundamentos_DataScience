import pandas as pd
from Leer_Limpiar import df

#I. Promedio, mediana y desviacion estandar de ataque por cada tipo principal (Tipo 1)
Estadisticas_Ataque_Por_Tipo = df.groupby('Tipo 1')['Ataque'].agg(['mean', 'median', 'std']).round(1)
Estadisticas_Ataque_Por_Tipo.columns = ['Promedio', 'Mediana', 'Desviacion_Estandar']

print(f"\nEstadisticas de Ataque por Tipo Principal:\n")
print(Estadisticas_Ataque_Por_Tipo.sort_values('Promedio', ascending=False))

#II. Tipo con mayor promedio de velocidad
Promedio_Velocidad_Por_Tipo = df.groupby('Tipo 1')['Velocidad'].mean().round(1)
Tipo_Mayor_Velocidad = Promedio_Velocidad_Por_Tipo.idxmax()
Valor_Mayor_Velocidad = Promedio_Velocidad_Por_Tipo.max()

print(f"\nPromedio de Velocidad por Tipo Principal:\n")
print(Promedio_Velocidad_Por_Tipo.sort_values(ascending=False))

print(f"\nEl tipo con mayor promedio de velocidad es: {Tipo_Mayor_Velocidad}")
print(f"Promedio de velocidad: {Valor_Mayor_Velocidad}")

#III. Para cada tipo principal, Pokemon con mayor y menor PS
print(f"\nPokemon con Mayor y Menor PS por Tipo Principal:\n")

for tipo in df['Tipo 1'].dropna().unique():
    Pokemones_Tipo = df[df['Tipo 1'] == tipo]
    
    # Pokemon con mayor PS del tipo
    Mayor_PS = Pokemones_Tipo[Pokemones_Tipo['PS'] == Pokemones_Tipo['PS'].max()]
    Pokemon_Mayor_PS = Mayor_PS.iloc[0]
    
    # Pokemon con menor PS del tipo
    Menor_PS = Pokemones_Tipo[Pokemones_Tipo['PS'] == Pokemones_Tipo['PS'].min()]
    Pokemon_Menor_PS = Menor_PS.iloc[0]
    
    print(f"Tipo {tipo}:")
    print(f"  Mayor PS: {Pokemon_Mayor_PS['Nombre']} (PS: {Pokemon_Mayor_PS['PS']})")
    print(f"  Menor PS: {Pokemon_Menor_PS['Nombre']} (PS: {Pokemon_Menor_PS['PS']})")
    print()

#IV. Resumen general por tipo
print(f"\nResumen General de Estadisticas por Tipo Principal:\n")
Resumen_Completo = df.groupby('Tipo 1')[['Ataque', 'Defensa', 'Velocidad', 'PS']].agg(['mean', 'std']).round(1)

print(Resumen_Completo)