# Trending Movies
This project is a web application that displays a movie, either from the trending movies through the TMDB website or from a list of movies included in the file through their TMDB Id's.  Each time the page is refreshed a new movie is shown.  For this version of the project I added a comment section as well as the ability to create users, login and comment on films.
##### View the website [here](https://trendingmovies.fly.dev)
## Project Overview
This project is built using Flask and is hosted on fly.io.
The project is divided into four main files:

- driver.py: This file is responsible for receiving data from the APIs and rendering the website
- TMDB_API.py: This file contains functions for interacting with [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)
- Wiki_API.py: This file contains functions for interacting with [Wikipedia's API](https://www.mediawiki.org/wiki/API:Main_page)
- database.py: This file creates the databases used for the comments and usernames.  It also contains the function that authenticates a user or chekcs if the user needs to be created.

## Required Technologies and Libraries
1. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.
2. To install Flask run `pip install Flask` in your terminal
3. Install flyctl using the apporpriate [method]("https://fly.io/docs/hands-on/install-flyctl/")
4. You will use the JSON, Random, OS, and Dotenv libraries which are included with Python.

## Installation and Setup

To run this project on your local machine, follow these steps:

1. Clone this repository to your local machine.
2. Make sure all appropriate technologies are installed
3. Create a .env file and put your TMDB API key in it.  The Wiki API does not require one.
4. In your .env file name the string for your api key TMDB_API_KEY.
5. Create a secret key for Flask and name it secret_key in your .env file.
6. You will need to launch a new app on fly.io and create a develop postgres database.
7. After that has been created and before launching change the postgres:// in your DATABASE_URL secret to be postgresql:// using fly secrets set.
8. If you would like to connect to the database or run the project on your local machine run the command `flyctl proxy 5432 -a <your databse name>`
9. You can then run the command `fly pg connect -a <your database name>` to connect to it remotely.
10. To run your website on your local machine run the command `FLASK_APP=<server file> DATABASE_URL=<connection string with localhost instead of your database> flask run`
11. With those commands you can now edit your website and database without having to deploy to fly.io any time you make a change.