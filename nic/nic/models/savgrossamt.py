from sqlalchemy import (
    Column,
    Index,
    Integer,
    ForeignKey,
    Text,
)

from .meta import Base
from .mymodel import login


class savGrossAmt(Base):
    __tablename__ = 'savings_gross_amt'
    id = Column(Integer, ForeignKey(login.id), primary_key=True)
    year = Column(Integer, primary_key=True)
    gamount= Column(Integer)
    #annualincome = Column(Integer)
