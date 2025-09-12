import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Leer_Limpiar import df

#Funcion del histograma, lo hice funcion para evitar errores y llamarlo mediante un print mas adelante.
def Histograma_Ataque():
    plt.figure('Histograma de Valores de Ataque')

    df['Ataque'].plot.hist(
    title='Distribución de Valores de Ataque de Pokemon',
    xlabel='Valor de Ataque',
    ylabel='Frecuencia (Número de Pokemon)',
    grid=True)

    plt.show()

#Funcion del Grafico de dispercion.
def Gdispercion_Ataque_Velocidad():

    df.plot.scatter(x='Ataque', y='Velocidad', 
                    title='Relación entre Ataque y Velocidad de Pokemon',
                    xlabel='Valor de Ataque',
                    ylabel='Valor de Velocidad',
                    grid=True)
    
    plt.show()

#Funcion de Boxplot de los PS por tipo principal
def Boxplot_PS_Tipo():
    
    df.boxplot(column='PS', by='Tipo 1', grid=True)
    
    plt.xlabel('Tipo Principal')
    plt.ylabel('Puntos de Salud')

    
    plt.show()

#Funcion del Violin plot de Defensa
def Violinplot_Defensa():
    plt.figure('Distribucion de Defensa - Violin Plot')
    
    sns.violinplot(data=df, y='Defensa')
    plt.title('Distribución de Defensa de Pokemon')
    plt.xlabel('Densidad')
    plt.ylabel('Valor de Defensa')
    plt.grid(True, alpha=0.3)
    
    plt.show()


#Mostrar las diferentes figuras
Histograma_Ataque()
Gdispercion_Ataque_Velocidad()
Boxplot_PS_Tipo()
Violinplot_Defensa()
            