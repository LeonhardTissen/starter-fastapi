from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Load the JSON file containing all words
with open('words_alpha.json') as f:
	words = json.load(f)

# Add CORS middleware to allow any origin
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_methods=['*'],
	allow_headers=['*'],
)

@app.get('/ww/check')
async def check_word(word: str = Query(...)):
	if word in words:
		return {'result': True}
	else:
		return {'result': False}

@app.get('/ww/match')
async def get_matching_word(word: str = Query(...), length: int = Query(0, gt=0), reverse: bool = Query(False)):
	for w in words:
		if len(w) == length and (w.startswith(word) or (reverse and w.endswith(word))):
			return {'matching_word': w}
	
	return {'message': 'No matching word found'}
