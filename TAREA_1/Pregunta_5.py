#5. Entrega un listado ordenado (de mayor a menos) de los estudiantes según su promedio

#Importo Diccionario de datos
import Diccionario as dc
estudiantes = dc.Estudiantes

#Diccionario para el promedio
Promedio_Notas = []

#Ciclo para calcular promedio
for estudiante in estudiantes:
    promedio = sum(estudiante['notas']) / len(estudiante['notas'])
    Promedio_Notas.append({'nombre': estudiante['nombre'], 'promedio': promedio})

#funcion Sorted para ordenar la lista de menor a mayor
Lista_Ordenada = sorted(Promedio_Notas, key=lambda estudiante: estudiante['promedio'], reverse = True)

#Imprime la lista ordenada
print('\nV. Listado ordenado de notas:\n')
for estudiante in Lista_Ordenada :
    print(f" - {estudiante['nombre']}: {estudiante['promedio']:.1f}")