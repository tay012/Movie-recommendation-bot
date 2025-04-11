import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

def build_movie_tuple(movie):
    """
    Helper to build a uniform 5-element tuple for a movie:
    (title, release_date, rating, overview, poster_url)
    """
    title = movie.get("title", "Untitled")
    release_date = movie.get("release_date", "Unknown")
    rating = movie.get("vote_average", "N/A")
    overview = movie.get("overview", "No overview available.")
    poster_path = movie.get("poster_path")
    poster_url = IMAGE_BASE_URL + poster_path if poster_path else None
    return (title, release_date, rating, overview, poster_url)

def search_by_title(title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title,
        "page": 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return f"No movies found matching '{title}'."
    
    top_movies = data["results"][:5]
    results = [build_movie_tuple(movie) for movie in top_movies]
    return results

def search_by_actor(actor_name):
    # First, search for the actor to get their ID.
    search_url = f"{BASE_URL}/search/person"
    search_params = {
        "api_key": API_KEY,
        "query": actor_name,
        "page": 1
    }
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()
    
    if "results" not in search_data or len(search_data["results"]) == 0:
        return f"No actor found for '{actor_name}'."
    
    actor = search_data["results"][0]
    actor_id = actor["id"]

    # Discover movies featuring the actor.
    discover_url = f"{BASE_URL}/discover/movie"
    discover_params = {
        "api_key": API_KEY,
        "with_cast": actor_id,
        "sort_by": "popularity.desc"
    }
    discover_response = requests.get(discover_url, params=discover_params)
    discover_data = discover_response.json()

    if "results" not in discover_data or len(discover_data["results"]) == 0:
        return f"No movies found for actor '{actor_name}'."
    
    top_movies = discover_data["results"][:5]
    results = [build_movie_tuple(movie) for movie in top_movies]
    return results

def search_by_genre(genre_name):
    # Map some common genres to TMDB genre IDs.
    genre_map = {
        "action": 28,
        "comedy": 35,
        "drama": 18,
        "horror": 27,
        "romance": 10749,
        "animation": 16,
        "sci-fi": 878
    }
    genre_id = genre_map.get(genre_name.lower())
    if not genre_id:
        return f"Sorry, genre '{genre_name}' not found."
    
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "sort_by": "popularity.desc"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "results" not in data:
        return "Something went wrong with the API request."
    
    top_movies = data["results"][:5]
    results = [build_movie_tuple(movie) for movie in top_movies]
    return results

def search_by_mood(mood):
    # Map moods to genres
    mood_to_genre = {
        "happy": "comedy",
        "excited": "action",
        "romantic": "romance",
        "sad": "drama",
        "scared": "horror",
        "adventurous": "action",  # Adjust mapping as needed.
        "curious": "sci-fi"
    }
    genre = mood_to_genre.get(mood.lower())
    if not genre:
        valid_moods = ", ".join(mood_to_genre.keys())
        return f"Sorry, I don't have recommendations for the mood '{mood}'. Try one of these moods: {valid_moods}."
    # Delegate mood-based search to genre search.
    return search_by_genre(genre)

def random_recommendation():
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": API_KEY, "page": 1}
    response = requests.get(url, params=params)
    data = response.json()
    
    if "results" not in data or len(data["results"]) == 0:
        return "No movies found."
    
    movie = random.choice(data["results"])
    return build_movie_tuple(movie)
