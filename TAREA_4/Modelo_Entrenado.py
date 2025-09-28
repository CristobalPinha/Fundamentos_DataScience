import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


''' 1 Datos y DataFrame - Universidad de Chile temporada 2024/25 Hasta el partido vs Coquimbo unido
    Datos extraidos de la página oficial de ESPN https://www.espn.cl/futbol/equipo/resultados/_/id/4139/liga/CHI.1
    Tanto los datos de la Universidad de chile como los de la serena de las últimas 10 fechas.


'''
datos = {
    #Datos de la Universidad de Chile Las 10 ultimas fechas.
    'Goles_anotados': [0, 1, 4, 0, 4, 2, 2, 2, 3, 0],
    'Tiros_A_Gol': [2, 5, 8, 4, 8, 5, 4, 4, 9, 3],
    'Tiro_Realizados': [12, 19, 24, 25, 17, 10, 10, 12, 23, 11],
    'Tiros_Esquina': [7, 8, 5, 11, 3, 3, 1, 3, 7, 4],
    'Posesion': [34.2, 68.5, 53.2, 66.1, 70, 59.3, 44.2, 43.1, 66.4, 63.5],
    'Es_Local': [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],

    #Datos de la Serena
    'Goles_Recibidos_Serena': [3, 2, 1, 3, 1, 2, 2, 1, 2, 4]}

df = pd.DataFrame(datos)

# 2. Definir X e Y (usando múltiples variables como el ejercicio original tenía potencial)
X = df[['Tiros_A_Gol', 'Tiro_Realizados', 'Tiros_Esquina', 'Posesion', 'Es_Local', 'Goles_Recibidos_Serena']]
Y = df['Goles_anotados']

# 3. Dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# 4. Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, Y_train)

# 5. Hacer predicciones
Y_pred = modelo.predict(X_test)

rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
r2 = r2_score(Y_test, Y_pred)

print(f'\nResultados de la evaluación (Goles vs Variables de Juego):\n')
print(f'RMSE: {rmse:.2f} en promedio, las predicciones se desvían en {rmse:.2f} goles')
print(f'R²: {r2:.2f}, (El {r2:.0%} de la variabilidad de goles se explica por las variables de juego)')

"""
CONCLUSION SOBRE LA PRECISION DEL MODELO:

El modelo de machine learning entrenado con los datos historicos de la Universidad de Chile
muestra un rendimiento ACEPTABLE para la prediccion de goles en futbol.

RMSE de 0.69: Significa que en promedio, nuestras predicciones se equivocan por 0.69 goles.
Para el contexto futbolistico, esto es BUENO, ya que los partidos de futbol tipicamente
tienen resultados entre 0-4 goles, por lo que un error de 0.69 goles es razonable.

R² de 0.30: Indica que el 30% de las variaciones en los goles se explican por nuestras
variables (tiros, posesion, localia, etc.). El 70% restante se debe a factores
no considerados como: suerte, errores arbitrales, clima, lesiones, motivacion.

INTERPRETACION: Un R² del 30% en futbol es DECENTE, porque el futbol tiene mucho
factor aleatorio. Los mejores modelos deportivos raramente superan el 60-70%.
Pero al solo contar con los ultimo 10 partidos de la pagina oficial de ESPN
obtenemos estos datos. Con mas datos resultados e informacion puede subir considerablemente
mas, es decir si hubiera utilizado unos 20 datos por cada uno y no 10, tendriamos un aprox
de 40-50% mas quizas de acierto

CONFIANZA: Las predicciones del modelo son CONFIABLES para tomar decisiones informadas,
pero siempre considerar que el futbol puede ser impredecible. Al menos en estos casos con
informacion reducida.
"""
