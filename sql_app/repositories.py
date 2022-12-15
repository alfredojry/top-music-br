from sqlalchemy.orm import Session

from .models import Song

class SongRepository:
    @staticmethod
    def find_all(db: Session) -> list[Song]:
        return db.query(Song).all()
    
    @staticmethod
    def save(db: Session, song: Song) -> Song:
        if song.id:
            db.merge(song)
        else:
            db.add(song)
        db.commit()
        return song
    
    @staticmethod
    def find_by_id(db: Session, id: int) -> Song:
        return db.query(Song).filter(Song.id == id).first()

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        song = db.query(Song).filter(Song.id == id).first()
        if song is not None:
            db.delete(song)
            db.commit()
