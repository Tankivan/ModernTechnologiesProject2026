from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import  List

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

@app.get("/")
async def main_page():
    return "This is main page of site!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)