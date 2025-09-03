#5. Entrega un listado ordenado (de mayor a menos) de los estudiantes según su promedio

#Importar pandas
import pandas as pd
df = pd.read_csv('Tarea_2/estudiante.csv')

#Guardar Notas en un arreglo
Notas = ['nota1', 'nota2', 'nota3', 'nota4']

#Revisar si faltan datos
hay_faltantes = df[Notas].isnull().sum().sum() > 0

#Calcular promedio
df['promedio'] = df[Notas].mean(axis=1).round(1)

df_ordenado = df.sort_values(by="promedio", ascending=False)

#Copia los datos para cambiarles el nombre a las columnas
df_mostrar = df_ordenado.copy()
df_mostrar.columns = ['Estudiante', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Promedio']

#Casos base
if not Notas:
    print(f'No hay Notas')
    
if hay_faltantes:
    print("Hay datos faltantes en el archivo")
    
else:
    #Muestra los nombres de los estudiantes y su promedio
    print(f'\nLista de estudiantes:')
    print(f'\n{df_mostrar[['Estudiante', 'Promedio']]}')
