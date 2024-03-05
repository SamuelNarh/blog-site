from fastapi import FastAPI
from db import models
from db.database import engine
from routers import blog
from fastapi.staticfiles import StaticFiles
#Midddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(blog.router)


#Database Creation
models.Base.metadata.create_all(engine)

# Static Files
app.mount('/images', StaticFiles(directory='images'),name='images')

#Middleware
origin =[
'http://localhost:3000'
]
app.add_middleware(
CORSMiddleware,
allow_origins=origin,
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*']
)