from fastapi import FastAPI
from app.routers import posts, categories, todo

app = FastAPI(
    title="Blog API",
    version="1.0.0"
)

# Routerlar
app.include_router(posts.router)
app.include_router(category.router)
app.include_router(todo.router)


@app.get("/")
def read_root():
    return {"xabar": "Blog API ga xush kelibsiz!"}