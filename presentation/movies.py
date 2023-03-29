from flask import Blueprint, jsonify
from business_logic.movies_service import get_characters,get_all_movies

movies_bp = Blueprint('movies_bp', __name__, url_prefix='')

@movies_bp.route('/', methods=['GET'])
def list_movies():
    movies = get_all_movies()
    return jsonify(movies)

@movies_bp.route('/<int:movie_id>/characters', methods=['GET'])
def list_characters(movie_id):
    characters = get_characters(movie_id)
    return jsonify(characters)