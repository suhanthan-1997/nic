from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    Date
)

from .meta import Base
from .mymodel import login


class DesigTable(Base):
    __tablename__ = 'desig_table'
    rec_id = Column(Integer, primary_key=True)
    id = Column(Integer, ForeignKey(login.id))
    designation = Column(Text)
    place_of_posting = Column(Text)
    date = Column(Date)
    emp_group = Column(Integer)
    
