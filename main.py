import ai_service
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
from schemas import ItemCreate, ItemOut
from typing import List
import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://ai-warehouse-inventory-frontend-mt9i6nw78.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Warehouse API is running"}

@app.get("/items", response_model=List[ItemOut])
def get_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.post("/items", response_model=ItemOut)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    item = crud.update_item(db, item_id, item)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}

@app.get("/ai/restock")
def restock_suggestions(db: Session = Depends(get_db)):
    low_stock = db.query(models.Item).filter(models.Item.quantity < 10).all()
    if not low_stock:
        return {"suggestions": [], "summary": "All items are well stocked!"}
    return ai_service.get_restock_suggestions(low_stock)
