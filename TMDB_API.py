import requests
import json
import random
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

tmdb_base_url = "https://api.themoviedb.org/3"


def get_trending_movie_id():
    # This function uses random to get one of the top 5 trending movies
    # It then finds the movie's id and returns that

    tmdb_trending_weekly_movies_path = "/trending/movie/week"
    random_trending_movie = random.randint(0, 4)

    trending_movies_response = requests.get(
        tmdb_base_url + tmdb_trending_weekly_movies_path,
        params={
            "api_key": getenv("TMDB_API_KEY"),
        },
    )

    trending_movies_id = trending_movies_response.json()["results"]
    return trending_movies_id[random_trending_movie]["id"]


def get_movie_by_id(movie_id):
    # This function takes in the id of a movie and grabs its information from the TMDB API
    # It then puts the required information into a dictionary and returns it

    movie_id_path = "/movie/{}".format(movie_id)

    id_movie_response = requests.get(
        tmdb_base_url + movie_id_path,
        params={
            "api_key": getenv("TMDB_API_KEY"),
        },
    )

    tmdb_image_base_url = "http://image.tmdb.org/t/p/"
    tmdb_image_size = "w342"

    id_movie_title = id_movie_response.json()["title"]
    id_movie_tagline = id_movie_response.json()["tagline"]
    if id_movie_tagline == "":
        id_movie_tagline = "This movie has no tagline"
    id_movie_genre = id_movie_response.json()["genres"][0]["name"]
    id_movie_overview = id_movie_response.json()["overview"]
    id_poster_path = id_movie_response.json()["poster_path"]
    id_movie_release_year = id_movie_response.json()["release_date"][:4]

    id_poster = tmdb_image_base_url + tmdb_image_size + id_poster_path

    id_movie_data = {
        "title": id_movie_title,
        "tagline": id_movie_tagline,
        "genres": id_movie_genre,
        "overview": id_movie_overview,
        "poster": id_poster,
        "year": id_movie_release_year,
        "id": movie_id,
    }
    return id_movie_data


def choose_harcode_or_trending():
    # This function uses a random number to pass trending id or random hardcoded id into get_movie_by_id
    # It then copies that into a dictionary and returns it

    hardcode_movie_ids = [218, 5548, 105, 244786, 78, 747, 577922, 710, 36557, 37724]
    movie_id_index = random.randint(0, 9)

    trending_id = get_trending_movie_id()

    trending_or_list = random.randint(0, 1)
    if trending_or_list == 0:
        return get_movie_by_id(trending_id)
    else:
        return get_movie_by_id(hardcode_movie_ids[movie_id_index])
