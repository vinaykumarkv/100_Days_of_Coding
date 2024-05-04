import requests
from bs4 import BeautifulSoup
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sys.path.insert(1, '/Users/vinay/PycharmProjects')
import creds

clientID = creds.spotify_clientID
password = creds.spotify_password
redirect_URL = "https://www.spotify.com/"
user_id =  creds.spotify_userID

# code for getting top 100 music for specific date

date = input("Enter your date of selection in format yyyy-mm-dd: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
print(url)
response = requests.get(url)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
movies = soup.find_all(name="h3", id="title-of-a-story",
                       class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
movie_list = [a.getText() for a in movies]
new_movie_list = []
for movie in movie_list:
	new_movie_list.append(movie.replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t", ""))
movie_list = []
for movie in new_movie_list:
	movie_list.append(movie.replace("\t\t\n\t\n", ""))
print(movie_list)

me_url = f"https://api.spotify.com/v1/me"
uid = "31lhdkonpcfzgdun6bmlh245hpee"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                                    client_secret=password,
                                                    redirect_uri=redirect_URL,
                                                    scope="playlist-modify-private"))
response = spotify.user_playlist_create(uid, f"Billboard to Spotify {date}", public=False, collaborative=False,
                                        description='')
playlist_ID = response['id']
tracks = []
for movie in movie_list:
	response = spotify.search(movie, limit=10, offset=0, type='track', market=None)
	url1 = response['tracks']['items'][0]['uri']
	print(url1)
	tracks.append(url1)
spotify.playlist_add_items(playlist_ID, tracks)
