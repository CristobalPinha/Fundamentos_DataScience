'''
Una corredora de propiedades en Santiago quiere predecir el precio (en UF) de departamentos. Tienen los siguientes datos:
datos = {'Superficie_m2': [50, 70, 65, 90, 45], 
        'Num_Habitaciones': [1, 2, 2, 3, 1], 
        'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0], 
        'Precio_UF': [2500, 3800, 3500, 5200, 2100]}
Construye un modelo de regresión lineal múltiple para predecir el 'Precio_UF' y evalúa su rendimiento.
'''

#Librerias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

#Datos
datos = {'Superficie_m2': [50, 70, 65, 90, 45],
         'Num_Habitaciones': [1, 2, 2, 3, 1],
         'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0],
         'Precio_UF': [2500, 3800, 3500, 5200, 2100]}

#Crear DataFrame
df = pd.DataFrame(datos)

#Definir X e Y
X = df[['Superficie_m2', 'Num_Habitaciones', 'Distancia_Metro_km']]
Y = df['Precio_UF']

#Dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

#Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, Y_train)

#Hacer predicciones
Y_pred = modelo.predict(X_test)

# 5. Hacer predicciones
Y_pred = modelo.predict(X_test)

rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
r2 = r2_score(Y_test, Y_pred)

print("\nResultados de la evaluación (Precio_UF vs Características del Departamento):")

print(f"\nError cuadrático medio: {rmse:.2f}")
print(f"R^2: {r2:.2f}\n")