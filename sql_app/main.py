from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .models import Song
from .database import engine, Base, get_db
from .repositories import SongRepository
from .schemas import SongRequest, SongResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/songs', response_model=list[SongResponse])
def find_all(db: Session = Depends(get_db)):
    songs = SongRepository.find_all(db)
    return [SongResponse.from_orm(song) for song in songs]
