#4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?

import pandas as pd
df = pd.read_csv('TAREA_2/estudiante.csv')

#Guardar Notas en un arreglo
Notas = ['nota1', 'nota2', 'nota3', 'nota4']

#Revisar si faltan datos
hay_faltantes = df[Notas].isnull().sum().sum() > 0

# Verificar si al menos una nota es < 4.0 y calcular su porcetanje
EstudiantesNotaBaja = (df[Notas] < 4.0).any(axis=1)

Porcentaje = (EstudiantesNotaBaja).mean()*100

#Casos base
if not Notas:
    print(f'No hay Notas')
    
if hay_faltantes:
    print("Hay datos faltantes en el archivo")

if Porcentaje == 0:
    print("No hay Estudiantes con notas menor a 4")
    
else:
    #Porcentaje y cantidad de estudiantes
    print(f'La cantidad de estudiantes con nota menor a 4.0 son:{len(df[EstudiantesNotaBaja])}')
    print(f'El porcentaje que los representa es:{Porcentaje}%')
    
