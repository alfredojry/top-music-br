import sys

sys.path.append('.')

from sql_app.repositories import SongRepository
from sql_app.models import Song
from sql_app.database import get_db
from sql_app.schemas import SongResponse

print('Hello, World!')

db = get_db()
songs = SongRepository.find_all(next(db))
data = [SongResponse.from_orm(song) for song in songs]
print(data)

