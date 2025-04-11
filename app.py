from flask import Flask, render_template, request, redirect, url_for
from tmdb_api import search_by_genre, search_by_actor, search_by_mood, search_by_title, random_recommendation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_type = request.form.get('search_type')
    
    if search_type == 'actor':
        actor_name = request.form.get('actor_name')
        results = search_by_actor(actor_name)
    elif search_type == 'mood':
        mood = request.form.get('mood')
        results = search_by_mood(mood)
    elif search_type == 'title':
        title = request.form.get('title')
        results = search_by_title(title)
    elif search_type == 'random':
        results = [random_recommendation()]
    elif search_type == 'genre':
        genre = request.form.get('genre')
        results = search_by_genre(genre)
    else:
        results = "Invalid search type."
    
    return render_template('results.html', results=results, search_type=search_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

