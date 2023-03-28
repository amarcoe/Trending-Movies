import flask
import TMDB_API
import Wiki_API

app = flask.Flask(__name__)


@app.route("/")
def index():
    movie_data = TMDB_API.choose_harcode_or_trending()
    wiki_page_url = Wiki_API.get_wiki_url(movie_data["title"], movie_data["year"])
    return flask.render_template(
        "index.html", movie_data=movie_data, wiki_page_url=wiki_page_url
    )


# app.run(debug=False)
