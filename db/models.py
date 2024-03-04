from db.database import Base

from sqlalchemy import Column,String,Integer, DateTime

class DBPost(Base):
    __tablename__= "posts"
    id= Column ( Integer , primary_key = True , index=True)  
    image_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column (String)
    timestamp = Column(DateTime)
    
