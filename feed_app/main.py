import sys

sys.path.append('.')

from sql_app.repositories import SongRepository
from sql_app.database import get_db, Base
from sql_app.schemas import SongResponse, SongRequest
from sql_app.models import Song
from scrapping import exec_scrapping

songs_lst = exec_scrapping()

"""
Base.metadata.create_all(bind=engine)

db = get_db()

for song in songs_lst:
    SongRepository.save(next(db), Song(**song))

songs = SongRepository.find_all(next(db))
data = [SongResponse.from_orm(song) for song in songs]

print(data)
"""
