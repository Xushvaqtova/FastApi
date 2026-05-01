from fastapi import FastAPI
from .routers import posts, todo, category

app = FastAPI(
    title="Blog API",
    description="FastAPI bilan yaratilgan loyiha",
    version="1.0.0"
)

# Routers
app.include_router(posts.router)
app.include_router(todo.router)
app.include_router(category.router)

@app.get("/")
def root():
    return {"xabar": "API ishlayapti 🚀"}