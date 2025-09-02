#1. Calcula el promedio de notas de cada estudiante y determina quién tiene promedio mas alto y mas bajo

#Importación de datos del archivo Diccionario.py
import Diccionario as dc
estudiantes = dc.Estudiantes

#Diccionario para el promedio
Promedio_Notas = []

#Ciclo para calcular promedio
for estudiante in estudiantes:
    promedio = sum(estudiante['notas']) / len(estudiante['notas'])
    Promedio_Notas.append({'nombre': estudiante['nombre'], 'promedio': promedio})

'''
#Ver a cada estudiante y su promedio
print(f'Promedio de cada estudiante:')
for estudiante in Promedio_Notas:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.1f}")
'''

#Calcular promedio con las funciones max y min    
PromedioAlto = max(Promedio_Notas, key=lambda estudiante: estudiante["promedio"])
PromedioBajo = min(Promedio_Notas, key=lambda estudiante: estudiante["promedio"])

#Imprimir los resultados
print(f"I. ¿Quién tiene el promedio mas alto, y mas bajo?")
print(f" - El promedio mas alto es: {PromedioAlto['nombre']}, {PromedioAlto['promedio']:.1f}")
print(f" - El promedio mas bajo es: {PromedioBajo['nombre']}, {PromedioBajo['promedio']:.1f}")