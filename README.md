# Movie Recommendation Bot

Movie Recommendation Bot is a fun and interactive web application built with Flask that provides movie suggestions based on your mood, actor, genre, or title search. It leverages the TMDB API to retrieve movie details—including title, release date, rating, overview, and poster images—and presents them in a modern, animated user interface using Bootstrap (with a Bootswatch theme) and Animate.css.

## Features

- **Multi-criteria Search:** Find movie recommendations by genre, actor, mood, title, or get a random suggestion.
- **Dynamic, Responsive UI:** A modern interface with animations, card layouts, and interactive modals for detailed movie information.
- **Poster Images:** Display movie posters (with a fallback placeholder if a poster isn’t available).
- **Local Custom Domain Support:** Optionally use custom hosts file entries (like `moviebot.local`) for local development.
- **Optional Tunneling:** Easily share your local development instance using LocalTunnel without hosting publicly.

## Technologies Used

- **Backend:** Python, Flask, Requests, python-dotenv
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5 (Bootswatch Cosmo theme), Animate.css
- **APIs:** The Movie Database (TMDB) API
- **Utilities:** LocalTunnel (for development access across devices)
- **Version Control:** Git and GitHub

## Prerequisites

- **Python 3.8+**
- **Node.js and npm** (if you plan to use LocalTunnel)
- A **TMDB API key** (Sign up at [TMDB](https://www.themoviedb.org/))

## Getting Started

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-bot.git
cd movie-recommendation-bot
2. Set Up the Virtual Environment
On Windows:

bash
Copy
python -m venv venv
venv\Scripts\activate
On macOS/Linux:

bash
Copy
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
pip install -r requirements.txt
Ensure your requirements.txt includes:

Flask

requests

python-dotenv

4. Configure Environment Variables
Create a .env file in the root of the project and add your TMDB API key:

env
Copy
TMDB_API_KEY=your_tmdb_api_key_here
You can also include a sample file (.env.example) to guide contributors:

env
Copy
TMDB_API_KEY=YOUR_TMDB_API_KEY
5. Run the Application
Start the Flask server by running:

bash
Copy
python app.py
By default, the app will be accessible at http://127.0.0.1:5000. For local network access, ensure your app.py uses:

python
Copy
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
6. (Optional) Expose the App with LocalTunnel
If you want to access your app from other devices, run:

bash
Copy
npx localtunnel --port 5000
This provides a public URL (e.g., https://awesome-alpaca.loca.lt) that you can use on your phone or share with others.

Usage
Open your browser to the app’s URL.

Choose a search type: genre, actor, mood, title, or random.

Input your query (for example, enter "comedy" for genre or "Tom Hanks" for actor).

View the movie recommendations complete with poster images and brief details.

Click on “More Details” to view additional movie information in a pop-up modal.

Contributing
Contributions are welcome! If you have suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request. Here’s a quick guide:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Commit your changes with clear messages.

Push to your fork and open a pull request.

License
This project is open-source under the MIT License.

