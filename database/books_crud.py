
from fastapi import HTTPException, status
from .models import BookIn, BookDb

books = [
    {"id": 0, "author": "Lars Kepler", "title": "Hämähäkki"},
    {"id": 1, "author": "Margaret Atwood", "title": "Orjattaresi"},
    {"id": 2, "author": "Lars Kepler", "title": "Nukkumatti"},
    {"id": 3, "author": "Paula Hawkins", "title": "Nainen junassa"},
    {"id": 4, "author": "Robert Galbraith", "title": "Käen kutsu"},
    {"id": 5, "author": "Irvine Welsh", "title": "Paska"},
    {"id": 6, "author": "Irvine Welsh", "title": "Mestarikokkien sänkykamarisalaisuudet"}
]




def create_book(book_in: BookIn):
    biggest = 0
    for book in books:
        if book["id"] > biggest:
            biggest = book["id"]
    new_id = biggest+1
    new_book = BookDb(id = new_id, **book_in.model_dump())
    books.append(new_book.model_dump())
    return new_book
            
            

def get_all_books(author: str = None):
    authorsBooks = []
    if author is not None:
        for book in books:
            if book["author"].strip().lower() == author.strip().lower():
                authorsBooks.append(book)
        return authorsBooks
    else:
        return books


def get_book_by_id(book_id: int):
    if len(books) != 0:
        for book in books:
            if book["id"] == book_id:
                return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found"
        )

def delete_book(book_id: int):
    index = 0
    book_found = False
    for book in books:
        if book["id"] == book_id:
            book_found = True
            break
        else:
            index+=1
    if book_found == False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found")
    del books[index]
