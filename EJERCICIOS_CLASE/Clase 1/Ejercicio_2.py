#datos
notas_curso = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2]
suma = 0
nota_alta = max(notas_curso)
nota_baja = min(notas_curso)
notas5 = 0
for notas in notas_curso:
    if notas >= 5.0:
        notas5 += 1
    suma += notas
promedio = suma / len(notas_curso)

print(f"Promedio:", (round(promedio, 1)))
print(f"la nota mas alta es:", nota_alta)
print(f"la nota mas baja es:",  nota_baja)
print(f"Estudiantes sobre 5.0:", notas5)