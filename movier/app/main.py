import pandas as pd
import uvicorn as uvicorn
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware
from resolver import random_items
from resolver import random_genres_items
from recommender import item_based_recommendation

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return{"message": "Hello 박소민의 영화추천 서비스"}

@app.get("/all/")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre:str):
    result = random_genres_items(genre)
    return {"result" : result}

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)