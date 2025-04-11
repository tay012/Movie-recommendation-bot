def save_to_watchlist(movie_tuple):
    """
    Save a given movie recommendation to a local watchlist file.
    Expects a 4-element tuple: (title, release_date, rating, overview).
    """
    title, release_date, rating, _ = movie_tuple
    with open("watchlist.txt", "a", encoding="utf-8") as f:
        f.write(f"{title} (Released: {release_date}, Rating: {rating})\n")
    print(f"Saved '{title}' to your watchlist!")
