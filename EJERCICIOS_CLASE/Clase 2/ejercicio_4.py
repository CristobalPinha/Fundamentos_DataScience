import numpy as np

grado_c = [0, 15, 25, 30, 100]
array_grados = np.array(grado_c)

grado_f = grado_c * (9/5) + 32


matriz = np.arange(1, 10).reshape(3, 3)
print("Matriz Original:\n", matriz)

# a) Elemento específico
elemento = matriz[1, 2]
print("\na) Elemento en la fila 2, columna 3:", elemento) 

# b) Segunda fila
fila_2 = matriz[1, :]
print("b) Segunda fila completa:", fila_2)

# c) Tercera columna
columna_3 = matriz[:, 2]
print("c) Tercera columna completa:", columna_3)
                