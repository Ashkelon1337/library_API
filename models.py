from database import Base
from sqlalchemy.types import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel


class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(100))
    year: Mapped[int | None] = mapped_column()
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)

class BookCreate(BaseModel):
    title: str
    author: str
    year: int | None = None

class BookResponse(BookCreate):
    id: int
    is_read: bool