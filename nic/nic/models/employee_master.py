from sqlalchemy import (
    Column,
    Index,
    Integer,
    ForeignKey,
    Text,
)

from .meta import Base
from .mymodel import login


class employee_master(Base):
    __tablename__ = 'employee_master'
    id = Column(Integer, ForeignKey(login.id), primary_key=True)
    name = Column(Text)
    father_name = Column(Text)
    address = Column(Text)
    gender = Column(Text)


