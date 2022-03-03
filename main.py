from os import name
from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from db import models
from db.database import engine
from routers import user, post, comment
from fastapi.staticfiles import StaticFiles
from auth import authentication
from starlette.middleware.cors import CORSMiddleware


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
  'http://localhost:3002',
  'https://8000-943de7fb-6564-44eb-800c-dcc4c7d84338.cs-us-east1-pkhd.cloudshell.dev'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
