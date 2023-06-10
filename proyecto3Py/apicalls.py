import requests
import json
def buscar_rating(id):
    url = "https://imdb8.p.rapidapi.com/title/get-ratings"

    querystring = {"tconst":id}

    headers = {
        "X-RapidAPI-Key": "9f65919693mshab9a818ee8efa24p1cd5a6jsn9a0cae0d7737",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response_json = response.json()

    title = response_json['title']
    rating = response_json['rating']
    rating_count = response_json['ratingCount']

    return[title, rating, rating_count]

"""     
    
    # Filtrar las cadenas que contienen '/title/'
    ids_filtradas = list(filter(lambda cadena: '/title/' in cadena, ids))

    ids_a_buscar = list(map(lambda id: id.replace('/title/', '').replace('/', ''), ids_filtradas))
     """

def buscar_titulo(title):
    url = "https://imdb8.p.rapidapi.com/title/find"

    querystring = {"q":title}

    headers = {
        "X-RapidAPI-Key": "9f65919693mshab9a818ee8efa24p1cd5a6jsn9a0cae0d7737",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    response_json = response.json()
    data = response_json['results']

    ids = list(map(lambda movie: movie['id'], data))
    
    # Filtrar las cadenas que contienen '/title/'
    ids_filtradas = list(filter(lambda cadena: '/title/' in cadena, ids))

    ids_a_buscar = list(map(lambda id: id.replace('/title/', '').replace('/', ''), ids_filtradas))
    
    return(ids_a_buscar)