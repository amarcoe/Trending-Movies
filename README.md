# project2-Alex-Marcoe
This project is a web application that displays a movie, either from the trending movies through the TMDB website or from a list of movies included in the file through their TMDB Id's.  Each time the page is refreshed a new movie is shown.  For this version of the project I added a comment section as well as the ability to create users, login and comment on films with those being saved to your username.
##### View the website [here](https://aged-cloud-145.fly.dev)
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
8. If you would like to connect to the database on your local machine run the command `flyctl proxy 5432 -a <your databse name>`
9. You can then run the command `fly pg connect -a <your database name>` to connect to it remotely.
10. To run your website on your local machine run the command `FLASK_APP=<server file> DATABASE_URL=<connection string with localhost instead of your database> flask run`
11. With those commands you can now edit your website and database without having to deploy to fly.io any time you make a change.

# Where my project differed from expectation
- The biggest way my project differed from my expectation was in the implementation of my index function.  I thought I was going to route every instance of rendering my index.html file through that function and I tried to make that work.  This led to issues with my methods and trying to force it to work.
- Another way it differed is with my databases.  In my original design I was going to have one database for all the users.  As I began thinking about the comment section I realized I didn't want to continuously update the comment column in the database if someone decided to make multiple comments.  I came up with the solution of making a new entry for each comment and then querying the database by the movie id so every comment under that woud be displayed but then the usernames wouldn't be unique and there could be multiple accounts with the same username.  Flask login was helpful in this as I was able to authenticate in one database and use current_user to add to the second one allowing for multiple entries from the same user with the guarantee that the username was unique.


Detailed description of 2+ technical issues and how you solved them (your process, what you searched, what resources you used)

## Technical Issues Experienced 
- The biggest issue I faced was having to rework my driver file.  In my original project I was able to make everything work with only one route and working on this project made me get a deeper understanding of Flask and routes.  The issue that caused the most difficulty for me was not knowing that I misunderstood how to transfer information using forms.  I was originally trying to send all the information similar to how I did the create account but that caused a lot of issues.  After using google and ChatGPT I realized that if I just directed it to the comment route without specifically sending the information that the information from the form still followed it to the new route.
- Another issue that I faced was setting up the new_comment route.  I knew from my design stage that I wanted the website to reload the page with the same movie when a comment was submitted.  I thought I would be able to do this using the same index route to for displaying a random movie or reloading the same one with a new comment.  I foolishly tried to force the function to work for way too long before accepting that I needed to rework the logic.  This also led me to rework the form action.  When I reworked the logic I realized that I was wrong to try posting in the index function because I needed the post to go to comments.  I realized this by rereading the demo that we got in class for the authentication which helped me see I was doing the action wrong.  Once I realized I couldn't do both things in one function I took a step back and realized I needed two routes.  This also led to the issue of being stuck in the new_comment route after a comment was posted which stopped the movies from randomly generating.  To fix this I made max_two to keep track of how many times the page was reloaded and if it was more than once it should route back to index.