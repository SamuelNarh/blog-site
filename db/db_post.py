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
    
def get_post(db:Session):
    all_post= db.query(DBPost).all()
    return all_post
