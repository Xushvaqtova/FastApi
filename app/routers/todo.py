from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

class Todo(BaseModel):
    title: str
    completed: bool = False

todos_db = []
todo_id = 1

# CREATE
@router.post("/")
def create_todo(todo: Todo):
    global todo_id
    t = todo.dict()
    t["id"] = todo_id
    todo_id += 1
    todos_db.append(t)
    return t

# READ
@router.get("/")
def get_todos():
    return todos_db

# UPDATE
@router.put("/{id}")
def update_todo(id: int, todo: Todo):
    for index, t in enumerate(todos_db):
        if t["id"] == id:
            new_t = todo.dict()
            new_t["id"] = id
            todos_db[index] = new_t
            return new_t
    raise HTTPException(status_code=404, detail="Todo topilmadi")

# DELETE
@router.delete("/{id}")
def delete_todo(id: int):
    for index, t in enumerate(todos_db):
        if t["id"] == id:
            todos_db.pop(index)
            return {"xabar": "O'chirildi"}
    raise HTTPException(status_code=404, detail="Todo topilmadi")