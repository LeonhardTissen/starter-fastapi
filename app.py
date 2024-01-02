from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import json

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    item_id: int


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Load the JSON file containing all words
with open('/words_alpha.json') as f:
	words = json.load(f)

@app.get('/checkword')
async def check_word(word: str = Query(...)):
    if word in words:
        return {'result': True}
    else:
        return {'result': False}

@app.get('/getmatchingword')
async def get_matching_word(word: str = Query(...), length: int = Query(0, gt=0), reverse: bool = Query(False)):
    for w in words:
        if len(w) == length and (w.startswith(word) or (reverse and w.endswith(word))):
            return {'matching_word': w}
    
    return {'message': 'No matching word found'}
