from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int

db = {}
next_id = 0

@app.post("/books")
def create_book(book: Book):
    global next_id
    db[next_id] = book
    next_id += 1
    return {"message": f"Added {book.title} with id {next_id - 1}"}

@app.get("/books")
def get_all_books():
    return db

@app.get("/books/{id}")
def get_book(id : int):
    if id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    return db[id]

@app.put("/books/{id}")
def update_book(id : int, book : Book):
    if id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    old_book = db[id]
    db[id] = book
    return {"message": f"Updated book {id}"}

@app.delete("/books/{id}")
def remove_book(id : int):
    if id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    del db[id]
    return {"message": f"Deleted book {id}"}
