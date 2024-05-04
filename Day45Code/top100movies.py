from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_list = [a.getText() for a in movies]
movie_list.reverse()
print(movie_list)

with open ("movielist.txt","w",encoding="utf8") as datafile:
	for line in movie_list:
		datafile.write(f"{line}\n")

