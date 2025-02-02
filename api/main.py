from fastapi import FastAPI, Request
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON file
with open("q-vercel-python.json") as f:
    student_marks = json.load(f)

@app.get("/")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_marks.get(name, None) for name in names]
    return {"marks": marks}

