import requests



def get_movies():
    movie_url = "https://swapi.dev/api/films/"
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    return sorted(movies,key=lambda x: x['id'])
    
def get_characters(movie_id):
    movie_url = f"https://swapi.dev/api/films/{movie_id}/"
    movie_data = requests.get(movie_url).json()
    characters = []
    for character_url in movie_data["characters"]:
        character_data = requests.get(character_url).json()
        characters.append(character_data["name"])
    return characters