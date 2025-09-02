#3. ¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?

#Importación de datos del archivo Diccionario.py
import Diccionario as dc
estudiantes = dc.Estudiantes

#Calcular la moda de todas las notas individuales
Totalidad_Notas = []
for estudiante in estudiantes:
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

