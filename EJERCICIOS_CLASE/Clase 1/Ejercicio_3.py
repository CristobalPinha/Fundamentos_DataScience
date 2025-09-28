#Datos
notas_curso = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0, 6.5]

#Tramos y limpieza de datos <==== IMPORTANTE LIMPIAR DATOS PARA EVITAR ERRORES
Reprobados = []
Aprobados = []
Destacados = []

#Almacenar Datos
for notas in notas_curso:
    if notas < 4.0:
        Reprobados.append(notas)
    if 4.0 <= notas <=5.9:
        Aprobados.append(notas)
    elif notas >= 6.0:
        Destacados.append(notas)

#Promedios
PromedioR = sum(Reprobados) / len(Reprobados)
PromedioA = sum(Aprobados) / len(Aprobados)
PromedioD = sum(Destacados) / len(Destacados)

#Porcentaje
PorcentajeR = len(Reprobados) / len(notas_curso) * 100
PorcentajeA = len(Aprobados) / len(notas_curso) * 100
PorcentajeD = len(Destacados) / len(notas_curso) * 100

#
print(f"La cantidad de reprobados son: [{(len(Reprobados))}] Su promedio: [{(PromedioR)}] Y su porcentaje es: [{(PorcentajeR)}%]")