from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import requests

from vector_store import VectorStore

app = FastAPI()

import os

app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(os.getcwd(), "templates"))

API_KEY = "773da9aacb98421b827e6f3408ed401c"

db = VectorStore()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "articles": [],
        "query": ""
    })

@app.post("/search", response_class=HTMLResponse)
def search(request: Request, query: str = Form(...)):

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": "India",
        "apiKey": API_KEY,
        "language": "en",
        "pageSize": 20
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = data.get("articles", [])

    db.vectors.clear()

    for article in articles:
        title = article.get("title", "")
        if title:
            db.add(title, article)

    results = db.search(query)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "articles": results,
        "query": query
    })