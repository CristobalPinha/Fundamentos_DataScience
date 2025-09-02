#2. Cuenta cuántos estudiantes aprobaron todas sus asignaturas (Todas las notas >= 4.0)

#Importación de datos del archivo Diccionario.py
import Diccionario as dc
estudiantes = dc.Estudiantes

#Diccionarios para guardar estudiantes con ciertas características
Todo_Aprobado = []
Alguno_Reprobado = []

#Analizar estudiantes que cumplan con las condiciones
for estudiante in estudiantes:
    if any(nota < 4.0 for nota in estudiante['notas']):
        Alguno_Reprobado.append(estudiante)
    else:
        Todo_Aprobado.append(estudiante)

print(f'II. ¿Cuántos estudiantes aprobaron todas sus asignaturas?')
#Imprimir los estudiantes que cumplen con las condiciones solicitadas
print(f' - Estudiantes con todos los ramos aprobados: {len(Todo_Aprobado)}')
for estudiante in Todo_Aprobado:
    print(f"{estudiante['nombre']}: {estudiante['notas']}")

#Imprimir los estudiantes que NO cumplen con las condiciones solicitadas
print(f'\n - Estudiantes con uno o mas ramos reprobados: {len(Alguno_Reprobado)}')
for estudiante in Alguno_Reprobado:
    print(f"{estudiante['nombre']}: {estudiante['notas']}")