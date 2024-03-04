from fastapi import FastAPI
from db import models
from db.database import engine
from routers import blog

app = FastAPI()

app.include_router(blog.router)


#Database Creation
models.Base.metadata.create_all(engine)