from os import name
from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from db import models
from db.database import engine
from routers import user, post, comment
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

@app.get("/")
def root():
  return "Hello world!"


origins = [
  'http://localhost:3000',
  'http://localhost:3001',
  'http://localhost:3002'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS", "DELETE", "PUT"],
    allow_headers=[
      #  "Access-Control-Allow-Headers",
        "Origin",
        "Accept",
        "X-Requested-With",
      #  "Content-Type",
        "Access-Control-Request-Method",
      #  "Access-Control-Request-Headers",
     #   "Access-Control-Allow-Origin",
     #   "Access-Control-Allow-Methods"
        "Authorization",
        "X-Amz-Date",
        "X-Api-Key",
        "X-Amz-Security-Token"
    ]
)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
