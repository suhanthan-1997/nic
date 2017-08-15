from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)

from .meta import Base
from .mymodel import login


class ProfTax(Base):
    __tablename__ = 'prof_tax'
    id = Column(Integer, ForeignKey(login.id), primary_key=True)
    proftax = Column(Text)
