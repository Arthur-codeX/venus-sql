from sqlalchemy.orm import declarative_base

from sqlalchemy import Column,Integer,String,DateTime

from datetime import datetime 

Base=declarative_base()



class UserModal(Base):

    __tablename__='user'

    id=Column(Integer,primary_key=True)
    first_name=Column(String,nullable=False)
    last_name=Column(String,nullable=False)
    # age=Column(Integer,nullable=False,default=12)
    created_at=Column(DateTime,default=datetime.utcnow)