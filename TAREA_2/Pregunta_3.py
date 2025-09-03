#3. ¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?

import pandas as pd
df = pd.read_csv('TAREA_2/estudiante.csv')

#Guardar Notas en un arreglo
Notas = ['nota1', 'nota2', 'nota3', 'nota4']

#Revisar si faltan datos
hay_faltantes = df[Notas].isnull().sum().sum() > 0

# Moda de todas las notas juntas
Total_Notas = df[Notas].values.flatten()
serie_notas = pd.Series(Total_Notas)
moda = serie_notas.mode()

# Contar cuántas veces aparece la moda
frecuencias = serie_notas.value_counts()
veces_moda = frecuencias[moda[0]]

#Casos base
if not Notas:
    print('No hay columnas de notas')
elif hay_faltantes:
    print("Hay datos faltantes en el archivo")
else:
    #Imprime la moda de las notas
    print(f"Moda de todas las notas: {moda[0]:.1f}")
    print(f"La nota {moda[0]:.1f} aparece {veces_moda} veces")
    
    # Mostrar las 5 notas más frecuentes
    print("\nLas 5 notas más frecuentes:")
    print(frecuencias.head())