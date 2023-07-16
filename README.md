# Webscrap_IMDB

# Web Scraping IMDB's Top Rated Movies with Python

Web scraping is a powerful tool that allows us to extract and collect information from websites. In this project, we'll be using Python's **BeautifulSoup** and **requests** libraries to scrape the Top Rated Movies from IMDB.

## Getting Started

First, we need to import the necessary libraries:

```python
import requests
from bs4 import BeautifulSoup
```

Python’s requests library will be used to send requests to a website to retrieve information, while BeautifulSoup will parse and organize the data we receive.

## Sending an HTTP Request

Next, we send a request to IMDB's Top Rated Movies page:

```python
url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
```

## Parsing the HTML Content

We then use BeautifulSoup to parse the HTML content:

```python
soup = BeautifulSoup(response.text, 'html.parser')
```

## Extracting the Data

Once the data is parsed, we can extract the specific information we're interested in:

```python
# getting list of movies which are in div elements using class id
movies = soup.find_all('div', class_='sc-14dd939d-0 fBusXE cli-children')
```

## Cleaning and Printing the Data

We then clean up the data and print out the results:

```python
for movie in movies:
    # getting movie name which is in div element
    title  = movie.div.text
    # getting release year which is in next div and span element
    year = movie.div.find_next('div').span.text
    print(f'{title} ({year})')
```

## Saving the Data

Finally, we write the movie titles and years to a file:

```python
with open('imdb_movies.txt', 'w') as file:
    for movie in movies:
        title = movie.a.text
        year = movie.span.text.strip('()')
        file.write(f'{title} ({year})\n')
```

The output is a file named 'imdb_movies.txt' in your current directory. If you open this file, you'll see the same list of movie titles and years.

And that's it! You've just learned the basics of web scraping using Python. This technique can be applied to other websites as well. Happy scraping!

## Output

```java
1. The Shawshank Redemption (1994)
2. The Godfather (1972)
3. The Dark Knight (2008)
4. The Godfather Part II (1974)
.......
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
