from sqlmodel import SQLModel

class BookBase(SQLModel):
    author: str
    title: str

class BookDb(BookBase):
    id: int
    
class BookIn(BookBase):
    pass