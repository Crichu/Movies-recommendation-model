from fastapi import FastAPI

app = FastAPI()

import pandas as pd

movies = pd.read_csv('Movies ETL.csv', sep=',') 
credits = pd.read_csv('Credits ETL.csv', sep=',')
cast = pd.read_csv('Cast.csv', sep=',')
director = pd.read_csv('Director.csv', sep=',')


@app.get("/cantidad_filmaciones_mes/{Mes}")
def cantidad_filmaciones_mes(Mes):

    # Convertir el mes a minúsculas y capitalizar la primera letra
    Mes = Mes.lower().capitalize()

    #Cargo el DF => ya lo cargué al inicio
    #movies = pd.read_csv('Movies ETL.csv', sep=',')

    # Convertir la columna 'release_date' a tipo de dato datetime
    movies['release_date'] = pd.to_datetime(movies['release_date'])

    # Filtrar las películas que coinciden con el mes consultado. Para que reconozca los meses en Español tengo que usar el parámetro 'es_ES.utf8'.
    filmaciones_mes = movies[movies['release_date'].dt.month_name(locale='es_ES.utf8') == Mes]
    
    # Obtener la cantidad de filmaciones en el mes
    cantidad = len(filmaciones_mes)

    return {'Cantidad de películas estrenadas: ': cantidad, 'En el mes de ': Mes}