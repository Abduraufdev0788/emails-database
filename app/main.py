from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(engine)


@app.get("/")
async def read_root():
    return {"message": "Xush kelibsiz!"}