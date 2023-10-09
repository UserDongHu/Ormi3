from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

db = [
    {
        "id": 1,
        "title": "이번 공부 너무 재미있어요.",
        "description": "완전 내 스타일이야!",
        "url": "https://inf.run/MQAk",
        "tags": ["Python", "Programming", "Beginner"]
    },
    {
        "id": 2,
        "title": "웹 개발자가 되고 싶어요!",
        "description": "함께 해봐요!",
        "url": "https://inf.run/MQAk",
        "tags": ["Node.js", "Express", "Web Development"]
    },
    {
        "id": 3,
        "title": "데이터 과학자가 되고 싶어요!",
        "description": "같이 준비해봅시다!",
        "url": "https://inf.run/mDME",
        "tags": ["Data Science", "Python", "Statistics"]
    }
]
app = FastAPI(docs_url="/documentation", redoc_url=None)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id, request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": db[int(item_id)]})
