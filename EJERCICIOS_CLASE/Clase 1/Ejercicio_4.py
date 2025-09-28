#Datos
Estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
    {"nombre": "Sofia", "notas": [3.9, 4.0, 4.5]},
    {"nombre": "Carlos", "notas": [5.5, 6.2, 6.8]},
    {"nombre": "María", "notas": [6.1, 5.9, 6.0]},
    {"nombre": "Diego", "notas": [4.8, 4.2, 5.0]},
    {"nombre": "Elena", "notas": [5.6, 6.4, 6.0]},
    {"nombre": "Pedro", "notas": [3.5, 2.0, 3.9]},
    {"nombre": "Lucía", "notas": [6.9, 6.7, 7.0]},
    {"nombre": "Mateo", "notas": [5.0, 5.2, 5.5]},
    {"nombre": "Valentina", "notas": [2.9, 3.8, 3.7]},
    {"nombre": "Javier", "notas": [6.0, 6.1, 5.9]},
    {"nombre": "Camila", "notas": [5.8, 5.7, 5.9]},
    {"nombre": "Andrés", "notas": [4.5, 4.8, 5.0]},
    {"nombre": "Isabella", "notas": [6.3, 6.6, 6.9]},
    {"nombre": "Ricardo", "notas": [3.7, 4.1, 3.9]},
    {"nombre": "Paula", "notas": [5.4, 5.2, 5.5]},
    {"nombre": "Fernando", "notas": [6.7, 6.5, 6.3]},
    {"nombre": "Daniela", "notas": [4.3, 4.5, 4.8]},
    {"nombre": "Gabriel", "notas": [5.1, 5.0, 5.3]},
    {"nombre": "Renata", "notas": [6.0, 6.4, 6.6]},
    {"nombre": "Hugo", "notas": [3.6, 3.9, 4.0]},
    {"nombre": "Natalia", "notas": [5.9, 6.1, 6.0]},
    {"nombre": "Marco", "notas": [4.0, 4.2, 4.1]},
    {"nombre": "Tomás", "notas": [5.5, 5.7, 5.6]},
    {"nombre": "Alicia", "notas": [4.7, 4.9, 5.0]},
    {"nombre": "Iván", "notas": [3.8, 3.6, 4.0]},
    {"nombre": "Clara", "notas": [6.2, 6.3, 6.1]},
    {"nombre": "Sebastián", "notas": [5.3, 5.4, 5.2]},
    {"nombre": "Cristobal", "notas": [7.0, 7.0, 7.0]},
]

#Promedio Total de cada estudiante
Promedio_Notas = []

#Calcular promedio
for estudiante in Estudiantes:
    promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
    Promedio_Notas.append({"nombre": estudiante["nombre"], "promedio": promedio})
    
'''
#Funcion que muestra el promedio final de cada estudiante
print("Promedio de notas de cada estudiante:")
for estudiante in Promedio_Notas:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.1f}")
'''

#Promedio Alto y Bajo
PromedioAlto = max(Promedio_Notas, key=lambda estudiante: estudiante["promedio"])
PromedioBajo = min(Promedio_Notas, key=lambda estudiante: estudiante["promedio"])
print(f"\nI. ¿Quién tiene el promedio más alto y quién el más bajo?")
print(f"El promedio mas alto es: {PromedioAlto['nombre']}, {PromedioAlto['promedio']:.1f}")
print(f"El promedio mas bajo es: {PromedioBajo['nombre']}, {PromedioBajo['promedio']:.1f}")

#Tramos estudiantes
Aprobados = []
Reprobados = []

#Funcion que separa los estudiantes en dos tramos, Aprobados y Reprobados.
for estudiante in Promedio_Notas:
    if estudiante["promedio"] >= 4.0:
        Aprobados.append(estudiante)
    elif estudiante["promedio"] < 4.0:
        Reprobados.append(estudiante)
        
#Imprime la cantidad de estudiantes aprobados y reprobados
print(f"\nII. ¿Cuántos estudiantes aprobaron?")
print(f"La cantidad de estudiantes aprobados es {len(Aprobados)}")
print(f"La cantidad de estudiantes Reprobados es {len(Reprobados)}")

'''       
#Revisar si los estudiantes aprobadon o no
print(f"Estudiantes Aprobados:")
for estudiante in Aprobados:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.1f}")

print(f"Estudiantes Reprobados:")
for estudiante in Reprobados:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.1f}")
''' 

#Calcular la moda de todas las notas individuales
Totalidad_Notas = []
for estudiante in Estudiantes:
    Totalidad_Notas.extend(estudiante["notas"]) # extend agrega los elementos de una lista a otra

# Método para calcular la moda
def Calcular_Moda(lista_notas):
    frecuencias = {}
    # Contar frecuencias
    for nota in lista_notas:
        if nota in frecuencias:
            frecuencias[nota] += 1
        else:
            frecuencias[nota] = 1        
    
    # Encontrar la frecuencia máxima
    max_frecuencia = max(frecuencias.values()) # values() devuelve solo los valores del diccionario
    
    # Encontrar todas las notas con esa frecuencia
    modas = [nota for nota, freq in frecuencias.items() if freq == max_frecuencia]

    return modas, max_frecuencia

# Calcular la moda y su frecuencia
Modas_Resultado, frecuencia = Calcular_Moda(Totalidad_Notas)

# Imprime la Moda y cuantas veces se repite
print(f"\nIII. ¿Cuál es la nota más frecuente considerando las notas de todos los estudiantes?")
print(f"La nota más frecuente es: {Modas_Resultado[0]}")
print(f"Se repite(n) {frecuencia} veces")


'''
# Mostrar todas las frecuencias hecho por copilot
print("\nFrecuencia de cada nota:")
frecuencias_todas = {}
for nota in todas_las_notas:
    if nota in frecuencias_todas:
        frecuencias_todas[nota] += 1
    else:
        frecuencias_todas[nota] = 1

# Ordenar por frecuencia (de mayor a menor)
for nota, freq in sorted(frecuencias_todas.items(), key=lambda x: x[1], reverse=True):
    print(f"Nota {nota}: aparece {freq} veces")

'''

# Función para calcular porcentaje de estudiantes con al menos una nota < 4.0
Estudiantes_Con_Nota_baja = []

for estudiante in Estudiantes:
    if any(nota < 4.0 for nota in estudiante["notas"]):
        Estudiantes_Con_Nota_baja.append(estudiante)
    else:
        pass
Porcentaje_Nota_Baja = (len(Estudiantes_Con_Nota_baja) / len(Estudiantes)) * 100

# Imprime el porcentaje de estudiantes con al menos una nota menor a 4.0
print(f"\nIV. ¿Qué porcentaje de estudiantes tienen al menos una nota menor a 4.0?")
print(f"La cantidad de estudiantes con al menos una nota menor a 4.0 es: {len(Estudiantes_Con_Nota_baja)}")
print(f"El porcentaje de estudiantes con al menos una nota menor a 4.0 es: {Porcentaje_Nota_Baja:.2f}%")

# Función alternativa que revisa notas y hace break al encontrar una nota < 4.0
def Revisar_Notas_Con_Break(lista_estudiantes):
    """
    Función que revisa las notas de los estudiantes y hace break 
    cuando encuentra al menos una nota menor a 4.0
    """
    estudiantes_con_nota_baja = []
    
    for estudiante in lista_estudiantes:
        print(f"Revisando estudiante: {estudiante['nombre']}")
        tiene_nota_baja = False
        
        # Revisar cada nota del estudiante
        for i, nota in enumerate(estudiante["notas"]):
            print(f"  Nota {i+1}: {nota}")
            if nota < 4.0:
                print(f"  ¡Encontrada nota menor a 4.0! ({nota})")
                estudiantes_con_nota_baja.append(estudiante)
                tiene_nota_baja = True
                break  # Sale del bucle de notas cuando encuentra una nota < 4.0
        
        if not tiene_nota_baja:
            print(f"  Todas las notas de {estudiante['nombre']} son >= 4.0")
        print()  # Línea en blanco para separar estudiantes
    
    return estudiantes_con_nota_baja

# Llamar a la función con break
print(f"\nIV.b Revisión de notas con break (función alternativa):")
print("=" * 60)
estudiantes_con_break = Revisar_Notas_Con_Break(Estudiantes)

print(f"Resumen:")
print(f"Estudiantes con al menos una nota < 4.0: {len(estudiantes_con_break)}")
for estudiante in estudiantes_con_break:
    print(f"- {estudiante['nombre']}")
print("=" * 60)

Lista_Ordenada = sorted(Estudiantes, key=lambda estudiante: sum(estudiante["notas"])/len(estudiante["notas"]), reverse=True) #Sorted ordena la lista de estudiantes por promedio de mayor a menor
print("\nV. Lista de estudiantes ordenada por promedio (de mayor a menor):")
for estudiante in Lista_Ordenada:
    print(f"{estudiante['nombre']}: {sum(estudiante['notas'])/len(estudiante['notas']):.1f}")