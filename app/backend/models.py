from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    password = Column(String)
    role = Column(String)

class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    content = Column(String)
    post_datetime = Column(DateTime)