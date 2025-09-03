#1. Calcula el promedio de notas de cada estudiante y determina quién tiene promedio mas alto y mas bajo

#Libreria pandas y leer el archivo .csv con datos
import pandas as pd
df = pd.read_csv('TAREA_2/estudiante.csv')

Notas = ['nota1', 'nota2', 'nota3', 'nota4']

hay_faltantes = df[Notas].isnull().sum().sum() > 0

#Funcion que calcula el promedio con mean(axis=1) para cada estudiante y redondea a 1 decima
df['promedio'] = df[Notas].mean(axis=1).round(1)

#Ambas funcionan para buscar el estudiante con el promedio mas alto y mas bajo
PromedioAlto = df.loc[df['promedio'].idxmax()]
PromedioBajo = df.loc[df['promedio'].idxmin()]

#Copia los datos para cambiarles el nombre a las columnas
df_mostrar = df.copy()
df_mostrar.columns = ['Estudiante', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Promedio']

#Casos base
if not Notas:
    print(f'No hay Notas')
    
if hay_faltantes:
    print("Hay datos faltantes en el archivo")
    
else:
    #Imprimir a los estudiantes con mejor y peor promedio
    print(f"I. ¿Quién tiene el promedio mas alto, y mas bajo?\n")

    print(f'ESTUDIANTE DESTACADO:\n')
    print(f" - Nombre: {PromedioAlto['nombre']}")
    print(f" - Promedio: {PromedioAlto['promedio']}")

    print(f'\nPROMEDIO MAS BAJO:\n')
    print(f" - Nombre: {PromedioBajo['nombre']}")
    print(f" - Promedio: {PromedioBajo['promedio']}")

    #Muestra los nombres de los estudiantes y su promedio
    print(f'\nLista de estudiantes:')
    print(f'\n{df_mostrar[['Estudiante', 'Promedio']]}')