from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    original_lyric = Column(String)
    br_lyric = Column(String)
    name_lyric = Column(String(100))
    band = Column(String(100))
    genres = Column(String(100))
