from fastapi import FastAPI

app = FastAPI(title="Информационный сайт по семестровому проекту", version="0.0.1")

@app.get("/")
async def main_page():
    return "This is main page of site!"