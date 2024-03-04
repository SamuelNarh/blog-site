from fastapi import HTTPException,status
from db.models import DBPost
from sqlalchemy.orm.session import Session
from schemas.schemas import PostBase
import datetime

def create_post(db:Session,request:PostBase):
    new_post = DBPost(
    image_url = request.image_url, 
    title = request.title,
    content = request.content,
    creator = request.creator,
    timestamp = datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    
def get_all(db:Session):
    all_post= db.query(DBPost).all()
    return all_post

def delete_post(db:Session, id:int):
    post = db.query(DBPost).filter(DBPost.id==id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id {id} not found',
        )
    
    db.delete(post)
    db.commit()
    return  "okay"
        