import sys
from bs4 import BeautifulSoup
import requests

sys.path.append('.')

from sql_app.repositories import SongRepository
from sql_app.database import get_db
from sql_app.schemas import SongResponse

print('Hello, World!')

db = get_db()
songs = SongRepository.find_all(next(db))
data = [SongResponse.from_orm(song) for song in songs]
print(data)

BASE_URL = 'https://www.vagalume.com.br'
MAIN_URL = f"{BASE_URL}/top100/musicas/"

main_html = requests.get(MAIN_URL).content
main_soup = BeautifulSoup(main_html, 'html.parser')
song_anchors = main_soup.select('li.borderless a')
song_paths = [anchor.get('href') for anchor in song_anchors]

for path in song_paths:
    song_link = f"{BASE_URL}{path}"
    song_html = requests.get(song_link).content
    song_soup = BeautifulSoup(song_html, 'html.parser')
    print(song_soup.title)
