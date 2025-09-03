#2. Cuenta cuántos estudiantes aprobaron todas sus asignaturas (Todas las notas >= 4.0)

#Importar pandas
import pandas as pd
df = pd.read_csv('TAREA_2/estudiante.csv')

#Guardar Notas en un arreglo
Notas = ['nota1', 'nota2', 'nota3', 'nota4']

#Revisar si faltan datos
hay_faltantes = df[Notas].isnull().sum().sum() > 0

#Funcion para ver quien aprueba todos los ramos
df['todos_aprobados'] = (df[Notas] >= 4.0).all(axis=1)
df['todos_aprobados'] = df['todos_aprobados'].map({True: 'Sí', False: 'No'})
aprobados = (df['todos_aprobados'] == 'Sí').sum()

#Estetica de columnas
df_mostrar = df.copy()
df_mostrar.columns = ['Estudiante', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Todo Aprobado']

#Casos base
if not Notas:
    print(f'No hay Notas')
    
if hay_faltantes:
    print("Hay datos faltantes en el archivo")
    
else:
    #Imprimir respuesta
    print(f'Los estudiantes que aprobaron todas sus asignaturas son: {aprobados}')
    print(df_mostrar[['Estudiante', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Todo Aprobado']])




