from tmdb_api import search_by_genre, search_by_actor, search_by_mood, search_by_title, random_recommendation
from watchlist import save_to_watchlist  # Import the save_to_watchlist function
import sys

while True:
    print("\n--- New Search ---")
    search_type = input("Choose search type (genre, actor, mood, title, random) or type 'quit' to exit: ").strip().lower()
    if search_type == 'quit':
        sys.exit("Exiting Movie Recommender Bot. Thanks for using it!")
    
    # Determine which search function to use:
    if search_type == 'actor':
        actor_name = input("Enter the actor's name: ").strip()
        results = search_by_actor(actor_name)
    elif search_type == 'mood':
        mood = input("What mood are you feeling? (e.g. happy, excited, romantic, sad, scared, adventurous, curious): ").strip()
        results = search_by_mood(mood)
    elif search_type == 'title':
        title = input("Enter the movie title (or part of it): ").strip()
        results = search_by_title(title)
    elif search_type == 'random':
        # Wrap the single random recommendation in a list for consistency:
        results = [random_recommendation()]
    elif search_type == 'genre':
        genre = input("What genre are you in the mood for? (e.g. comedy, action, romance): ").strip()
        results = search_by_genre(genre)
    else:
        print("Invalid search type. Please choose from the provided options.")
        continue

    # Display the results:
    print("\nTop picks for you:\n")
    if isinstance(results, str):
        print(results)
    else:
        for i, item in enumerate(results, start=1):
            if search_type in ('title', 'random'):
                title, release_date, rating, overview = item
                print(f"{i}. {title} (Released: {release_date}, Rating: {rating})")
                print(f"   {overview[:150]}...\n")
            else:
                # For genre/actor/mood searches, our results are a tuple with title and overview:
                title, overview = item
                print(f"{i}. {title}\n   {overview[:150]}...\n")
    
    # Prompt the user if they want to save a movie to their watchlist:
    save_choice = input("Would you like to save any of these movies to your watchlist? Enter the number or press Enter to skip: ").strip()
    if save_choice.isdigit():
        index = int(save_choice) - 1
        if index < len(results):
            movie = results[index]
            # For functions that return only title and overview, convert to a 4-element tuple:
            if isinstance(movie, tuple) and len(movie) == 2:
                title, overview = movie
                movie_to_save = (title, "Unknown", "N/A", overview)
            else:
                movie_to_save = movie
            save_to_watchlist(movie_to_save)
