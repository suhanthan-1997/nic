from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class login1(Base):
    __tablename__ = 'login1'
    id = Column(Integer, primary_key=True)
    password = Column(Text)
