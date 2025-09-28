import pandas as pd

calificaciones = [7, 2, 8, 9, 3, 10, 6, 1, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4, 8, 7, 2, 9, 6, 10, 3, 5, 4]

# Pasar el array a un dataframe
df = pd.DataFrame(calificaciones, columns=['Calificacion'])

# Filtrar el DataFrame para que solo tenga valores entre 1 y 10
df = df[(df['Calificacion'] >= 1) & (df['Calificacion'] <= 10)]

# Calificación media
Media = df['Calificacion'].mean()

# Desviación estándar
DesviacionEstandar = df['Calificacion'].std()

# Calificación máxima
CalificacionMaxima = df['Calificacion'].max()
CalificacionMinima = df['Calificacion'].min()

# El numero de clientes que dieron una calificacion mayor a 8
ClientesMayores8 = df[df['Calificacion'] > 8]
NumeroClientesMayores8 = len(ClientesMayores8)

# Verificar si el DataFrame está vacío
if df.empty:
	print("El DataFrame está vacío.")

else:
	# Calificación media
	print("Calificación media:", Media)
	# Desviación estándar
	print("Desviación estándar:", DesviacionEstandar)
	# Calificación máxima
	print("Calificación máxima:", CalificacionMaxima)
	# Calificación mínima
	print("Calificación mínima:", CalificacionMinima)
	# Número de clientes que dieron una calificación mayor a 8
	print(f"Número de clientes que dieron una calificación mayor a 8: {NumeroClientesMayores8}")
