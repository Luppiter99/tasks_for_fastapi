from sqlalchemy import String, Integer, Column, ForeignKey

from app.backend.db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
