from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey
)

from .meta import Base
from .mymodel import login

class UserView(Base):
    __tablename__ = 'user_view'
    rec_id = Column(Integer, primary_key=True)
    id = Column(Integer, ForeignKey(login.id))
    group_view = Column(Integer)
