from fastapi import APIRouter, HTTPException, status
from typing import List
from ..schemas import Category

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

# 🗄 Fake DB
categories_db = []
category_id = 1

# =========================
# CREATE
# =========================
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_category(category: Category):
    global category_id

    cat_dict = category.dict()
    cat_dict["id"] = category_id
    category_id += 1

    categories_db.append(cat_dict)
    return cat_dict


# =========================
# READ ALL + PAGINATION
# =========================
@router.get("/", response_model=List[dict])
def get_categories(skip: int = 0, limit: int = 10):
    return categories_db[skip: skip + limit]


# =========================
# READ ONE
# =========================
@router.get("/{id}")
def get_category(id: int):
    for c in categories_db:
        if c["id"] == id:
            return c
    raise HTTPException(status_code=404, detail="Category topilmadi")


# =========================
# UPDATE
# =========================
@router.put("/{id}")
def update_category(id: int, category: Category):
    for index, c in enumerate(categories_db):
        if c["id"] == id:
            updated = category.dict()
            updated["id"] = id
            categories_db[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Category topilmadi")


# =========================
# DELETE
# =========================
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id: int):
    for index, c in enumerate(categories_db):
        if c["id"] == id:
            categories_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Category topilmadi")


# =========================
# SEARCH (UY ISHI QISMI)
# =========================
@router.get("/search/")
def search_category(q: str):
    natija = []

    for c in categories_db:
        if q.lower() in c["name"].lower() or q.lower() in c["description"].lower():
            natija.append(c)

    return {"natija": natija}