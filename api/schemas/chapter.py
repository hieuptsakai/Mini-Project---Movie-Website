from pydantic import BaseModel

class ChapterBase(BaseModel):
    chapter_num: int
    mangaid: int
    images: list[int] = []

class ChapterCreate(ChapterBase):
    pass

class Chapter(ChapterBase):

    class Config:
        orm_mode = True