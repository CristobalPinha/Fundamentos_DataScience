#4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?

#Importación de datos del archivo Diccionario.py
import Diccionario as dc
estudiantes = dc.Estudiantes

Nota_Baja = []

for estudiante in estudiantes:
    for nota in estudiante['notas']:
        if nota < 4.0:
            Nota_Baja.append({'nombre': estudiante['nombre'], 'notas': estudiante['notas'] })
            break

Porcentaje = len(Nota_Baja) / len(estudiantes) * 100

print(f'IV. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?')
print(f' - Porcentaje de estudiantes con nota menor a 4.0 es: {Porcentaje}%')
#Imprimir los estudiantes que cumplen con las condiciones solicitadas
print(f' - Estudiantes con notas < 4.0: {len(Nota_Baja)}\n')
for estudiante in Nota_Baja:
    print(f" - {estudiante['nombre']}: {estudiante['notas']}")

