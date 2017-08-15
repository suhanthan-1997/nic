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


class TaxPaid(Base):
    __tablename__ = 'tax_paid'
    rec_id = Column(Integer, primary_key=True)
    id = Column(Integer, ForeignKey(login.id))
    amt = Column(Integer)
    date = Column(Date)
    aca_year = Column(Text)
