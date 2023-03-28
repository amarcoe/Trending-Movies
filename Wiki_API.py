import requests
import json

wiki_base_url = "https://en.wikipedia.org/w/api.php"


def get_wiki_url(title, year):
    # This function gives the url for the movie's wikipedia page
    # It calls the get_wiki_title page to get the exact title for the page
    # It uses that to find and return the full url for the page

    movie_title = get_wiki_title(title, year)

    url_page_response = requests.get(
        wiki_base_url,
        params={
            "action": "query",
            "prop": "info",
            "format": "json",
            "titles": movie_title,
            "inprop": "url",
        },
    )

    page_url = url_page_response.json()["query"]["pages"]
    page_key = list(page_url.keys())

    return page_url[page_key[0]]["fullurl"]


def get_wiki_title(dynamic_title, dynamic_year):
    # This function uses the search query to get the exact title of the movie
    # Since some movies are remakes it's not guaranteed that the first search gives the movie
    # It then uses a for loop to look at all the titles from the search and find the one that best matches the movie
    # Once that has been found it returns it as a string

    movie_search_title = requests.get(
        wiki_base_url,
        params={
            "action": "query",
            "list": "search",
            "format": "json",
            "srsearch": dynamic_title,
        },
    )

    search_page = movie_search_title.json()["query"]["search"]
    search_key = list(search_page[0].keys())
    size = len(search_page)

    for i in range(size):
        if search_page[i][search_key[1]] == (
            dynamic_title + " (" + dynamic_year + " film)"
        ):
            page_title = search_page[i][search_key[1]]
            break
        elif search_page[i][search_key[1]] == (dynamic_title + " (film)"):
            page_title = search_page[i][search_key[1]]
            break
        elif search_page[i][search_key[1]] == (dynamic_title):
            page_title = search_page[i][search_key[1]]

    return page_title
