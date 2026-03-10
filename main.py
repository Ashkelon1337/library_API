from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
import uvicorn

from database import get_session, init_dp
from models import Book, BookCreate, BookResponse

app = FastAPI()
SessionDep = Annotated[AsyncSession, Depends(get_session)]

@app.on_event('startup')
async def create_db():
    await init_dp()
    print("✅ База данных готова")

@app.post('/books', response_model=BookResponse)
async def create_book(book_create: BookCreate, session: SessionDep):
    new_book = Book(
        title=book_create.title,
        author=book_create.author,
        year=book_create.year
    )
    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)
    return new_book

@app.get('/books', response_model=list[BookResponse])
async def get_books(session: SessionDep):
    data = await session.scalars(select(Book))
    return data.all()

@app.get('/books/{book_id}', response_model=BookResponse)
async def get_book(book_id: int, session: SessionDep):
    data = await session.scalar(select(Book).where(Book.id == book_id))
    if not data:
        raise HTTPException(status_code=404, detail='Книга не найдена')
    return data

@app.put('/books/{book_id}', response_model=BookResponse)
async def swap_is_reading(book_id: int, session: SessionDep):
    data = await session.scalar(select(Book).where(Book.id == book_id))
    if not data:
        raise HTTPException(status_code=404, detail='Книга не найдена')
    data.is_read = not data.is_read
    await session.commit()
    await session.refresh(data)
    return data

@app.delete('/books/{book_id}')
async def delete_book(book_id: int, session: SessionDep):
    data = await session.scalar(select(Book).where(Book.id == book_id))
    if not data:
        raise HTTPException(status_code=404, detail='Книга не найдена')
    await session.delete(data)
    await session.commit()
    return {'ok': True, 'message': f'Книга {book_id} успешно удалена!'}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)