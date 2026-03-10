# Library API

Простое API для управления книгами.

# Технологии
- FastAPI
- SQLAlchemy 2.0
- SQLite
- Pydantic

# Установка

### 1. Клонировать репозиторий

   git clone https://github.com/твой-логин/library-api.git
   cd library-api
### 2. Создать и активировать виртуальное окружение

    #Windows
    python -m venv venv
    venv\Scripts\activate

    #Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
### 3. Установить зависимости
    pip install -r requirements.txt
### 4. Запустить сервер
    python main.py
### 5. Открыть в браузере
    http://127.0.0.1:8000/docs

# Эндпоинты
- `POST /books` - создать книгу
- `GET /books` - все книги
- `GET /books/{id}` - одна книга
- `PUT /books/{id}` - отметить прочитанной
- `DELETE /books/{id}` - удалить