# Convencion par importar NumPy

import numpy as np

# Crear un array de NumPy desde una lista

lista_notas = [6.5, 7.0, 5.8, 4.9]
array_notas = np.array(lista_notas)

print(lista_notas)

# Simplemente sumamos 0.5 al array completo usando NumPy
notas_finales_np = array_notas + 0.5

print(notas_finales_np)