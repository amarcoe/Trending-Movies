import TMDB_API
import Wiki_API
import flask
import database
from os import getenv

app = flask.Flask(__name__)
app.secret_key = getenv("secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")


@app.route("/")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():
    form_data = flask.request.form  # This will give us all the form data from index
    username = form_data["username"]
    if authenticate_user(username):
        return flask.redirect(flask.url_for("index"))
    else:
        flask.flash(
            "That username doesn't exit, try typing it again or create an account."
        )
        return flask.redirect(flask.url_for("login"))
    # user.isAuthenticated is more how it's actually done but htis is easier for demo


@app.route("/index")
def index():
    movie_data = TMDB_API.choose_harcode_or_trending()
    wiki_page_url = Wiki_API.get_wiki_url(movie_data["title"], movie_data["year"])
    return flask.render_template(
        "index.html", movie_data=movie_data, wiki_page_url=wiki_page_url
    )


def authenticate_user(username):
    return username == "Alex"


app.run(debug=True)
