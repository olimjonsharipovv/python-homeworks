
import requests
import random

def get_movies_by_genre(api_key, genre_name):
    genre_url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {'api_key': api_key}
    
    try:
   
        response = requests.get(genre_url, params=params)
        response.raise_for_status()
        genres = response.json()['genres']
        
        # Find the genre ID for our genre name
        genre_id = None
        for genre in genres:
            if genre['name'].lower() == genre_name.lower():
                genre_id = genre['id']
                break
        
        if not genre_id:
            print(f"Genre '{genre_name}' not found.")
            return None
        
        # Now get movies by genre
        discover_url = "https://api.themoviedb.org/3/discover/movie"
        params = {
            'api_key': api_key,
            'with_genres': genre_id,
            'sort_by': 'popularity.desc',
            'page': random.randint(1, 5)  # Random page for variety
        }
        
        response = requests.get(discover_url, params=params)
        response.raise_for_status()
        movies = response.json()['results']
        
        if not movies:
            print(f"No movies found in genre '{genre_name}'.")
            return None
        
        # Return a random movie from the results
        return random.choice(movies)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie data: {e}")
        return None

def main():
    API_KEY = "your_api_key_here"
    
    print("Movie Recommendation System")
    genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    
    movie = get_movies_by_genre(API_KEY, genre)
    if movie:
        print("\nRecommended Movie:")
        print(f"Title: {movie['title']}")
        print(f"Release Date: {movie['release_date']}")
        print(f"Rating: {movie['vote_average']}/10")
        print(f"Overview: {movie['overview']}")

if __name__ == "__main__":
    main()















