import uvicorn
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException

from routers import users, type, manga, favorite, chapter

app = FastAPI()

@app.get("/")
def root_access():
    return {"message": "Hello World"}

app.include_router(users.router)
app.include_router(type.router)
app.include_router(manga.router)
app.include_router(favorite.router)
app.include_router(chapter.router)

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)