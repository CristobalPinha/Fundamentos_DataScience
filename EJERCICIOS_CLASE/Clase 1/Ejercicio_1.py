#datos
notas_curso = [6.5, 7.0, 3.2, 4.9, 5.8, 2.1, 4.0]
suma_total = 0
aprobados = 0

for notas in notas_curso:
    if notas >= 4.0:
        aprobados += 1
    suma_total += notas

promedio = suma_total / len(notas_curso)
print(promedio, aprobados)

