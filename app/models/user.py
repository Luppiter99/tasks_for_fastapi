from sqlalchemy import Column, String, Integer

from app.backend.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    password = Column(String)
