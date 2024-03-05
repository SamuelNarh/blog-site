import random
import shutil
from fastapi import APIRouter,Depends, File, UploadFile
from schemas.schemas import PostBase,PostDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_post
from typing import List
import string

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.post('/',response_model=PostDisplay)
def create_post(request:PostBase,db:Session = Depends(get_db)):
    return db_post.create_post(db,request)

@router.get('/all',response_model=List[PostDisplay])
def get_post(db:Session=Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}')
def delete_post(id:int, db:Session=Depends(get_db)):
    return db_post.delete_post(db,id)

#Image upload
@router.post('/images')
def upload_image(image:UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(10))  # Random alphanumeric string of length 10
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.',1))
    path= f'images/{filename}'
    
    with open (path,"w+b") as buffer:
        shutil.copyfileobj(image.file,buffer)
    
    return {'filename': path}