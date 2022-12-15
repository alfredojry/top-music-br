from pydantic import BaseModel

class SongBase(BaseModel):
    original_lyric: str
    br_lyric: str
    name_lyric: str
    band: str
    genres: str

class SongRequest(SongBase):
    pass

class SongResponse(SongBase):
    id: int

    class Config:
        orm_mode = True
