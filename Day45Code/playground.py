from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
article_tag = (soup.find_all(name="a"))
article_text = article_tag[11].getText()
article_link = article_tag[11].get("href")
artile_upvote = soup.find(name="span", class_="score").getText()
print(article_tag[11])
print(article_text)
print(article_link)
print(artile_upvote.split(" ")[0])

