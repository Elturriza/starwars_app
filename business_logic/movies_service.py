from data.movies_data import get_movies, get_characters

def get_all_movies():
    return get_movies()

def get_movie_characters(movie_id):
    return get_characters(movie_id)