from sqlalchemy.orm import Session
import models, schemas

def get_items(db: Session):
    return db.query(models.Item).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    new_item = models.Item(
        name=item.name,
        quantity=item.quantity,
        category=item.category
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, item_id:int, item:schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db_item.name = item.name
    db_item.quantity = item.quantity
    db_item.category = item.category

    db.commit()
    db.refresh(db_item)
    db.refresh

    return db_item


def delete_item(db: Session, item_id: int):
    item = get_item(db, item_id)
    if item:
        db.delete(item)
        db.commit()
        return True
    return False