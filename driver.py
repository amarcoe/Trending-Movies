import TMDB_API
import Wiki_API
import flask
import os
from database import create_table, Users, db
from flask_login import LoginManager, login_required, login_user, current_user

app = flask.Flask(__name__)
app.secret_key = os.getenv("secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


create_table(app)


@app.route("/")
def login():
    flask.session.clear()
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():
    form_data = flask.request.form
    username = form_data["username"]
    user = Users.authenticate(username)

    if "login" in flask.request.form:
        if user:
            login_user(user)
            return flask.redirect(flask.url_for("index"))
        else:
            flask.flash(
                "That username doesn't exit, try typing it again or create an account."
            )
            return flask.redirect(flask.url_for("login"))
    elif "create_account" in flask.request.form:
        if user:
            flask.flash("That account already exists, please login")
            return flask.redirect(flask.url_for("login"))
        else:
            return flask.redirect(flask.url_for("create_account", username=username))


@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    # I like getting information in the if statements but for post I need it.
    # I think I need to build database so I can see how that works with routing and such.
    if flask.request.method == "POST":
        movie_data = TMDB_API.get_movie_by_id(movie_id)
        wiki_page_url = Wiki_API.get_wiki_url(movie_data["title"], movie_data["year"])

        form_data = flask.request.form
        if "rating" not in form_data and "comment" not in form_data:
            flask.flash("Please rate and comment")
        elif "rating" not in form_data:
            flask.flash("Please rate the movie")
        elif "comment" not in form_data:
            flask.flash("Please leave a comment")
        else:
            # This will be go to leave_comment
            # Just getting it to work basic so I can start database
            return flask.redirect(flask.url_for("index"))

    else:
        movie_data = TMDB_API.choose_harcode_or_trending()
        wiki_page_url = Wiki_API.get_wiki_url(movie_data["title"], movie_data["year"])

        return flask.render_template(
            "index.html", movie_data=movie_data, wiki_page_url=wiki_page_url
        )


@app.route("/keep_movie_data/<movie_id>")
@login_required
def keep_movie_data(movie_id):
    movie_data = TMDB_API.get_movie_by_id(movie_id)
    wiki_page_url = Wiki_API.get_wiki_url(movie_data["title"], movie_data["year"])

    return flask.redirect(flask.url_for("comment", movie_id=movie_data["id"]))


@app.route("/comment/<username>/<movie_id>/<comments>/<ratings>")
@login_required
def leave_comment(comment):
    print("whatever")


#     username = db.Column(db.String(80), db.ForeignKey("Users.username"), nullable=False)
#     movie_id = db.Column(db.Integer, nullable=False)
#     comments = db.Column(db.String(500), nullable=False)
#     ratings = db.Column(db.Integer, nullable=False)


@app.route("/create/<username>")
def create_account(username):
    user = Users(username=username)
    db.session.add(user)
    db.session.commit()
    print(f"Created user with username {username}")
    login_user(user)
    return flask.redirect((flask.url_for("index")))


# app.run(debug=True)
