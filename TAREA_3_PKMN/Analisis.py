import pandas as pd
from Leer_Limpiar import df

#I. Analisis de tipos con mayor tendencia de ataque y defensa
def Analisis_Ataque_Defensa_Por_Tipo():
    print(f"\n=== ANÁLISIS DE ATAQUE Y DEFENSA POR TIPO ===")
    
    # Estadisticas de ataque por tipo
    Estadisticas_Ataque = df.groupby('Tipo 1')['Ataque'].agg(['mean', 'max', 'min']).round(1)
    Estadisticas_Ataque.columns = ['Promedio', 'Maximo', 'Minimo']
    
    print(f"\nESTADÍSTICAS DE ATAQUE POR TIPO:")
    print(Estadisticas_Ataque.sort_values('Promedio', ascending=False))
    
    # Estadisticas de defensa por tipo
    Estadisticas_Defensa = df.groupby('Tipo 1')['Defensa'].agg(['mean', 'max', 'min']).round(1)
    Estadisticas_Defensa.columns = ['Promedio', 'Maximo', 'Minimo']
    
    print(f"\nESTADÍSTICAS DE DEFENSA POR TIPO:")
    print(Estadisticas_Defensa.sort_values('Promedio', ascending=False))
    
    # Tipos con mayor ataque y defensa
    Tipo_Mayor_Ataque = Estadisticas_Ataque['Promedio'].idxmax()
    Valor_Mayor_Ataque = Estadisticas_Ataque['Promedio'].max()
    
    Tipo_Mayor_Defensa = Estadisticas_Defensa['Promedio'].idxmax()
    Valor_Mayor_Defensa = Estadisticas_Defensa['Promedio'].max()
    
    print(f"\nCONCLUSIÓN:")
    print(f"Tipo con mayor promedio de ATAQUE: {Tipo_Mayor_Ataque} ({Valor_Mayor_Ataque})")
    print(f"Tipo con mayor promedio de DEFENSA: {Tipo_Mayor_Defensa} ({Valor_Mayor_Defensa})")

#II. Correlacion entre ataque y velocidad
def Correlacion_Ataque_Velocidad():
    print(f"\n=== CORRELACIÓN ATAQUE Y VELOCIDAD ===")
    
    # Calcular correlacion
    Correlacion = df['Ataque'].corr(df['Velocidad']).round(3)
    
    print(f"\nCoeficiente de correlación entre Ataque y Velocidad: {Correlacion}")
    
    # Interpretacion de la correlacion
    if Correlacion > 0.7:
        Interpretacion = "FUERTE POSITIVA"
    elif Correlacion > 0.3:
        Interpretacion = "MODERADA POSITIVA"
    elif Correlacion > 0.1:
        Interpretacion = "DÉBIL POSITIVA"
    elif Correlacion > -0.1:
        Interpretacion = "MUY DÉBIL o NULA"
    elif Correlacion > -0.3:
        Interpretacion = "DÉBIL NEGATIVA"
    elif Correlacion > -0.7:
        Interpretacion = "MODERADA NEGATIVA"
    else:
        Interpretacion = "FUERTE NEGATIVA"
    
    print(f"Interpretación: Correlación {Interpretacion}")
    
    if Correlacion > 0:
        print(f"Existe una tendencia: a mayor ataque, mayor velocidad")
    elif Correlacion < 0:
        print(f"Existe una tendencia: a mayor ataque, menor velocidad")
    else:
        print(f"No existe relación lineal entre ataque y velocidad")

#III. Dispersion de PS por tipo
def Dispersion_PS_Por_Tipo():
    print(f"\n=== DISPERSIÓN DE PS POR TIPO ===")
    
    # Calcular estadisticas de dispersion
    Dispersion_PS = df.groupby('Tipo 1')['PS'].agg(['mean', 'std', 'min', 'max']).round(1)
    Dispersion_PS.columns = ['Promedio', 'Desviacion_Estandar', 'Minimo', 'Maximo']
    Dispersion_PS['Rango'] = Dispersion_PS['Maximo'] - Dispersion_PS['Minimo']
    
    print(f"\nDISPERSIÓN DE PS POR TIPO:")
    print(Dispersion_PS.sort_values('Desviacion_Estandar', ascending=False))
    
    # Tipos mas y menos dispersos
    Tipo_Mas_Disperso = Dispersion_PS['Desviacion_Estandar'].idxmax()
    Valor_Mas_Disperso = Dispersion_PS['Desviacion_Estandar'].max()
    
    Tipo_Menos_Disperso = Dispersion_PS['Desviacion_Estandar'].idxmin()
    Valor_Menos_Disperso = Dispersion_PS['Desviacion_Estandar'].min()
    
    print(f"\nCONCLUSIÓN:")
    print(f"Tipo MÁS disperso en PS: {Tipo_Mas_Disperso} (σ = {Valor_Mas_Disperso})")
    print(f"Tipo MENOS disperso en PS: {Tipo_Menos_Disperso} (σ = {Valor_Menos_Disperso})")
    print(f"\nInterpretación:")
    print(f"- {Tipo_Mas_Disperso}: Mayor variabilidad (pokémon muy diferentes en PS)")
    print(f"- {Tipo_Menos_Disperso}: Menor variabilidad (pokémon similares en PS)")

#IV. Identificacion de outliers en ataque y PS
def Identificar_Outliers():
    print(f"\n=== IDENTIFICACIÓN DE OUTLIERS ===")
    
    # Outliers en Ataque usando IQR
    Q1_Ataque = df['Ataque'].quantile(0.25)
    Q3_Ataque = df['Ataque'].quantile(0.75)
    IQR_Ataque = Q3_Ataque - Q1_Ataque
    Limite_Inferior_Ataque = Q1_Ataque - 1.5 * IQR_Ataque
    Limite_Superior_Ataque = Q3_Ataque + 1.5 * IQR_Ataque
    
    Outliers_Ataque = df[(df['Ataque'] < Limite_Inferior_Ataque) | (df['Ataque'] > Limite_Superior_Ataque)]
    
    print(f"\nOUTLIERS EN ATAQUE:")
    print(f"Límite inferior: {Limite_Inferior_Ataque:.1f}")
    print(f"Límite superior: {Limite_Superior_Ataque:.1f}")
    print(f"Cantidad de outliers: {len(Outliers_Ataque)}")
    
    if len(Outliers_Ataque) > 0:
        print(f"\nPokémon outliers en ATAQUE:")
        print(Outliers_Ataque[['Nombre', 'Tipo 1', 'Ataque']].sort_values('Ataque', ascending=False))
    
    # Outliers en PS usando IQR
    Q1_PS = df['PS'].quantile(0.25)
    Q3_PS = df['PS'].quantile(0.75)
    IQR_PS = Q3_PS - Q1_PS
    Limite_Inferior_PS = Q1_PS - 1.5 * IQR_PS
    Limite_Superior_PS = Q3_PS + 1.5 * IQR_PS
    
    Outliers_PS = df[(df['PS'] < Limite_Inferior_PS) | (df['PS'] > Limite_Superior_PS)]
    
    print(f"\nOUTLIERS EN PS:")
    print(f"Límite inferior: {Limite_Inferior_PS:.1f}")
    print(f"Límite superior: {Limite_Superior_PS:.1f}")
    print(f"Cantidad de outliers: {len(Outliers_PS)}")
    
    if len(Outliers_PS) > 0:
        print(f"\nPokémon outliers en PS:")
        print(Outliers_PS[['Nombre', 'Tipo 1', 'PS']].sort_values('PS', ascending=False))

# Ejecutar todas las funciones de analisis
print("ANÁLISIS EXPLORATORIO DE DATOS (EDA) - PREGUNTA 7")
print("=" * 55)

Analisis_Ataque_Defensa_Por_Tipo()
Correlacion_Ataque_Velocidad()
Dispersion_PS_Por_Tipo()
Identificar_Outliers()