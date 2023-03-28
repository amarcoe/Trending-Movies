# project1-Alex-Marcoe
This project is a web application that displays a movie, either from the trending movies through the TMDB website or from a list of movies included in the file through their TMDB Id's.  Each time the page is refreshed a new movie is shown.  
##### View the website [here](https://restless-water-893.fly.dev/)
## Project Overview
This project is built using Flask and is hosted on fly.io.
The project is divided into three main files:

- driver.py: This file is responsible for receiving data from the APIs and rendering the website
- TMDB_API.py: This file contains functions for interacting with [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)
- Wiki_API.py: This file contains functions for interacting with [Wikipedia's API](https://www.mediawiki.org/wiki/API:Main_page)

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
5. The project will now work on your local system when you run driver.


# Additional Features 
- I would like to add more information on the movies such as embedding their trailer, including actors and what streaming services they're available on.  All of this is available through the TMDB API, I just needed more time to implement this.  I would like to get access to the JustWatch API to include a more larger list of streaming services available, but I coulnd't, there is a free one on github, but it didn't have all the streaming services I wanted.
- I would also like to do more with the CSS on the website.  There are a lot of creative things you can do but I ran out of time to do all that is available.  I would rearrange how the data is displayed and also make the button look better through CSS as well as spending more time on the fonts and background.

## Technical Issues Experienced 
- The largest issue I had was getting information between the Wiki API file and TMDB API file.  In the original way I wrote the Wiki API it imported the dictionary returned by the TMDB API file.  This caused an issue where after refreshing the page the Wikipedia link wouldn't match the movie title.  I did a lot of searching trying to see if there was an issue with sharing information between files in a Flask app but couldn't find anything.  Since I couldn't find anything online I knew it had to be with my code so I put print statements in various places throughout my code to document the variable as it moved through my files and put flask into debug mode.  Through looking at the print statements and the debug log I learned the wikipedia url stopped updating.  When I couldn't find any information about the issue I decided to rewrite the function to take in arguments which would be given when it was called in the driver.py file.
- Another technical issue I faced was with the Wikipedia API.  Since Wikipedia is so large there are multiple things that can come up from one search, for example Casino Royale (one the movies I chose) is a novel, a movie from 1967 and a movie from 2006.  When I checked the link in my original code it took me to [this page]("https://en.wikipedia.org/wiki/Casino_Royale") so I knew I needed to find a way to find the definitive film I was looking for.  This led me to dig through the documentation more as my first query didn't show the search results of the page, just the url.  I found the srsearch in the list which gave me the contents of the search page as a json file.  With that I was able to use a for loop to look at all the search results and find the most accurate name for my movie since there are three options.  It will either be just the title, title (movie) or title (year movie).