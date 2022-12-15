import sys

sys.path.append('.')

from sql_app.repositories import SongRepository
from sql_app.database import get_db, Base, engine
from sql_app.schemas import SongResponse, SongRequest
from sql_app.models import Song
from scrapping import exec_scrapping

songs_lst = exec_scrapping()

Base.metadata.create_all(bind=engine)

db = next(get_db())
db.query(Song).delete()

for song in songs_lst:
    SongRepository.save(db, Song(**song))
