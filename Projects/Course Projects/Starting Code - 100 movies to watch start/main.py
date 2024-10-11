import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_web_page = response.text

# creating soup
soup = BeautifulSoup(empire_web_page, "lxml")

# creating movie list
movie_title_tags = soup.find_all(name="h3", class_="title")f
movie_list = [movie.getText() for movie in movie_title_tags]
movie_list.reverse() # reversing the list

# writing the movies in the .txt file
for movie in movie_list:
    try:
        with open(file="movies.txt", mode="a") as file:
            file.write(f"{movie}\n")
    except FileNotFoundError:
        with open(file="movies.txt", mode="w") as file:
            file.write(f"{movie}\n")
