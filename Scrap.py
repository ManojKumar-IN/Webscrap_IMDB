# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://www.imdb.com/chart/top'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all div elements with the specified class ID
# getting list of movies which are in div elements using class id
movies = soup.find_all('div', class_='sc-14dd939d-0 fBusXE cli-children')

for movie in movies:
    # getting movie name which is in div element
    title  = movie.div.text
    # getting release year which is in next div and span element
    year = movie.div.find_next('div').span.text
    print(f'{title} ({year})
