from flask import Flask, render_template
import urllib.request, json

import os

app = Flask(__name__)

app.config.update(
    TESTING=True,
    TMDB_API_KEY="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNDA5ZWUxMTZhMDZkZTZiMjhhN2JjYzVhNmM1N2M0MiIsInN1YiI6IjYyM2NjODg2ZmQ2ZmExMDA1Y2MyNDgyNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dTmRUJKvCBFCq8XBUx5ZCHVCZYJv3LNSpO62FB0Ak5A",
)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/")
def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(
        os.environ.get("TMDB_API_KEY")
    )

    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
    except Exception as e:
        print(e)

    # return dict
    return render_template("movies.html", movies=dict["results"])


@app.route("/movies")
def get_movies_list():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(
        os.environ.get("TMDB_API_KEY")
    )

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    movies = []

    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }

        movies.append(movie)

    return {"results": movies}


if __name__ == "__main__":

    app.run(debug=True)
