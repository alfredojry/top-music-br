import sys
from bs4 import BeautifulSoup
import requests

sys.path.append('.')

from sql_app.repositories import SongRepository
from sql_app.database import get_db
from sql_app.schemas import SongResponse

db = get_db()
songs = SongRepository.find_all(next(db))
data = [SongResponse.from_orm(song) for song in songs]

BASE_URL = 'https://www.vagalume.com.br'
MAIN_URL = f"{BASE_URL}/top100/musicas/"

main_html = requests.get(MAIN_URL).content
main_soup = BeautifulSoup(main_html, 'html.parser')
song_anchors = main_soup.select('li.borderless a')
song_paths = [anchor.get('href') for anchor in song_anchors]

songs_lst = []

for path in song_paths:
    song_link = f"{BASE_URL}{path}"
    song_html = requests.get(song_link).content
    song_soup = BeautifulSoup(song_html, 'html.parser')
    # Get name_lyric
    name_lyric = song_soup.title.text
    print(f"Extracting info for the song: {name_lyric}")
    # Handle original and translated lyrics
    original_lyric = ''
    br_lyric = ''
    div_liryc = song_soup.find(id='lyrics')
    if div_liryc:
        br_lyric = "\n".join(div_liryc.find_all(text=True))
    else:
        div_pairs = song_soup.find(id='lyricsPair')
        if div_pairs:
            br_lines = song_soup.select('.trad.pair')
            br_lyric = '\n'.join(line.string for line in br_lines)
            original_lines = song_soup.select('.orig.pair')
            original_lyric = ''.join(line.string for line in original_lines)
    # Get band name
    band = song_soup.find('a', { 'data-target': 'artBody' }).string
    # Get genres
    ul_tags = song_soup.find('ul', { 'class': ['subHeaderTags', 'h14'] })
    genres = ','.join(ul_tags.find_all(text=True))
    # Resume informations in a dict
    song_dict = {
        'name_liryc': name_lyric,
        'original_lyric': original_lyric,
        'br_lyric': br_lyric,
        'band': band,
        'genres': genres
    }

