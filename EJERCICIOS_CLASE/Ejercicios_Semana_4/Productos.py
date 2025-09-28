import numpy as np

precios = np.array([19990, 45500])
cantidad = np.array([10, 5])

# Calcular el ingreso total por producto
IngresoTotal = precios * cantidad

# Ingreso total del dia
IngresoTotalDia = np.sum(IngresoTotal)

# Descuento 10% a todos los precios
Descuento = precios * 0.10
PreciosConDescuento = precios - Descuento

#Si esta vacio el array retorna Vacio, si no retorna las funciones
if precios.size == 0:
    print("El array está vacío.")
else:
    print("\nIngreso total por producto:", IngresoTotal)
    print("\nIngreso total del día:", IngresoTotalDia)
    print("\nPrecios con descuento del 10%:\n", PreciosConDescuento)