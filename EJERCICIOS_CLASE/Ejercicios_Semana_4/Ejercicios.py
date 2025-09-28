import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 1 Datos y DataFrame
datos = {'Headshot_porc': [10, 15, 20, 25, 30, 8, 35, 28, 18, 23],
         'KD_Ratio': [0.7, 1.1, 1.4, 1.8, 2.2, 0.5, 2.9, 2.0, 1.3, 1.6]}

df = pd.DataFrame(datos)

# 2. Definir X e Y
X = df[['Headshot_porc']]
Y = df['KD_Ratio']

# 3. Dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
#print(X_train, X_test, Y_train, Y_test)

# 4. Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, Y_train)

# 5. Hacer predicciones
Y_pred = modelo.predict(X_test)

rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
r2 = r2_score(Y_test, Y_pred)

print(f'\nResultados de la evaluación (K/D vs % Headshot):\n')
print(f'RMSE: {rmse:.2f} en promedio, las predicciones se desvian en {rmse:.2f} puntos')
print(f'R²: {r2:.2f}, (El {r2:.0%} de la variabilidad de K/D se explica por el % de Headshot)')
