from fastapi import APIRouter,Depends
from schemas.schemas import PostBase,PostDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_post
from typing import List

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.post('/',response_model=PostDisplay)
def create_post(request:PostBase,db:Session = Depends(get_db)):
    return db_post.create_post(db,request)

@router.get('/all',response_model=List[PostDisplay])
def get_post(db:Session=Depends(get_db)):
    return db_post.get_post(db)