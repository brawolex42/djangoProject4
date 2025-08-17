
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Category
from schemas.question import CategoryCreate, CategoryUpdate, CategoryResponse
from database import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    exists = db.query(Category).filter(Category.name == payload.name).first()
    if exists:
        raise HTTPException(status_code=409, detail="category exists")
    obj = Category(name=payload.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).order_by(Category.name).all()

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, payload: CategoryUpdate, db: Session = Depends(get_db)):
    obj = db.query(Category).get(category_id)
    if not obj:
        raise HTTPException(status_code=404, detail="not found")
    if payload.name is not None:
        dup = db.query(Category).filter(Category.name == payload.name, Category.id != category_id).first()
        if dup:
            raise HTTPException(status_code=409, detail="name in use")
        obj.name = payload.name
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    obj = db.query(Category).get(category_id)
    if not obj:
        raise HTTPException(status_code=404, detail="not found")
    db.delete(obj)
    db.commit()
    return None
