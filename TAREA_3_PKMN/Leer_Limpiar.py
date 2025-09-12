import pandas as pd

#Mientras leo, filtro las columnas y datos vacios.
df = pd.read_csv('TAREA_3_PKMN/pokemon_primera_gen.csv',
                usecols=['Nombre', 'Tipo 1', 'Tipo 2', 'Ataque', 'Defensa', 'Velocidad', 'PS'],
                na_values=['', ' ', 'null', 'N/A'])

#Separo los datos por Tipo y Estadistica de cada Pokemon
Tipos = df[['Tipo 1', 'Tipo 2']]
Estadisticas = df[['Ataque', 'Defensa', 'Velocidad', 'PS']]

#Si alguna estadistica es negativa la corrige por su valor absoluto
df[Estadisticas.columns] = df[Estadisticas.columns].abs()

#Elimina los duplicados
df = df.drop_duplicates(subset=['Nombre'], keep='first')

#Pokemones validos en primera generacion, por ejemplo no existe el tipo hada.
Tipos_Validos = ['Bicho', 'Dragón', 'Eléctrico', 'Lucha', 'Fuego', 
                'Volador', 'Fantasma', 'Planta', 'Tierra', 'Hielo', 
                'Normal', 'Veneno', 'Psíquico', 'Roca', 'Agua']

#Si el tipo de Pokemon no es Valido, se reemplaza por vacio
df.loc[df['Tipo 1'].isin(Tipos_Validos) == False, 'Tipo 1'] = 'Normal'
df.loc[df['Tipo 2'].isin(Tipos_Validos) == False, 'Tipo 2'] = None

#Limpiar espacios extras o no deseados
df['Nombre'] = df['Nombre'].str.strip()
df['Nombre'] = df['Nombre'].str.replace(r'\s+', ' ', regex=True)

# Remover puntos (Mr. Mime = Mr Mime)
df['Nombre'] = df['Nombre'].str.replace('.', '', regex=False)

# Mantener solo letras, espacios, ♀, ♂, apóstrofes
df['Nombre'] = df['Nombre'].str.replace(r'[^a-zA-Z\s♀♂\']', '', regex=True)