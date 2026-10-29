from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import  List
from database import engine, get_db
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse, PostCreateResponse
import models

#пример класса для фронтенда. Будет потом изменён.
class Fruit(BaseModel):
    name: str
    price: float

class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI(title="Информационный сайт по семестровому проекту", version="0.0.1")


origins = [
    "http://localhost:5173"
]

# из видео (ссылка к нему будет прикреплена в описании коммита)
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],

)

#Часть датабазы. Не скопировал из видео, так как структура бд ещё не определена.

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def main_page():
    return "This is main page of site!"

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
  users = db.query(models.User).all()
  return users

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404, 
            detail="Пользователь не найден"
        )
        
    return user

@app.get("/posts/{post_id}", response_model=PostCreateResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(
            status_code=404, 
            detail="Пост не найден"
        )
            
    return post

@app.get("/posts/")
def read_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)