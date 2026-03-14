#cd C:\Users\roope\OneDrive\Työpöytä\SAMK-kurssit\backend-ohjelmointi.\.venv\Scripts\activate
#uv add "fastapi[standard]" --active
#fastapi dev Main.py
from fastapi import APIRouter,  status
from ..database import books_crud
from ..database.models import BookDb, BookIn
router = APIRouter(tags=["books"])




@router.post("/books", response_model=BookDb, status_code=status.HTTP_201_CREATED)
def create_shoe(book_in: BookIn):
    
    return books_crud.create_book(book_in)
            
            
@router.get("/books", response_model = list[BookDb])
def get_all_books(author: str = None):
    return books_crud.get_all_books(author)

@router.get("/books/{book_id}", response_model=BookDb,
        responses={
            404: {"description": "shoe not found"}
        })
def get_book_by_id(book_id: int):
    return books_crud.get_book_by_id(book_id)


@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    return books_crud.delete_book(book_id)
