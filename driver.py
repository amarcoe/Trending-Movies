import TMDB_API
import Wiki_API
import flask
import database
from flask_login import LoginManager, login_required

# from database import create_table, Person, db
from os import getenv

app = flask.Flask(__name__)
app.secret_key = getenv("secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

# login_manager = LoginManager()

db.init_app(app)
# login_manager.init_app(app)

create_table(app)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)


@app.route("/")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():
    form_data = flask.request.form
    username = form_data["username"]

    if "login" in flask.request.form:
        if authenticate(username):
            return flask.redirect(flask.url_for("index"))
        else:
            flask.flash(
                "That username doesn't exit, try typing it again or create an account."
            )
            return flask.redirect(flask.url_for("login"))
    elif "create_account" in flask.request.form:
        create_account = form_data["create_account"]
        if authenticate(username):
            flask.flash("That account already exists, please login")
            return flask.redirect(flask.url_for("login"))
        # else:
        # Create account
        # Need active database to continue


@app.route("/index")
def index():
    movie_data = TMDB_API.choose_harcode_or_trending()
    wiki_page_url = Wiki_API.get_wiki_url(movie_data["title"], movie_data["year"])
    return flask.render_template(
        "index.html", movie_data=movie_data, wiki_page_url=wiki_page_url
    )


# app.run(debug=True)
