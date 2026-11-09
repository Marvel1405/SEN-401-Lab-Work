"""
FastAPI RESTful web application providing CRUD endpoints for inventory management.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, DBItem

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SEN 401 Re-Engineered FastAPI Service", version="2.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the re-engineered SEN 401 FastAPI service!"}

@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    return db.query(DBItem).all()

@app.post("/items/")
def create_item(item_name: str, quantity: int, price: float, db: Session = Depends(get_db)):
    existing = db.query(DBItem).filter(DBItem.item_name == item_name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Item already exists")
    db_item = DBItem(item_name=item_name, quantity=quantity, price=price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"status": "success", "data": db_item}