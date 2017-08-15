from sqlalchemy import (
    Column,
    Index,
    Integer,
    ForeignKey,
    Text,
    Date
)

from .meta import Base
from .mymodel import login


class employee_salary(Base):
    __tablename__ = 'employee_salary'
    id = Column(Integer, ForeignKey(login.id), primary_key=True)
    salary = Column(Text)
    da = Column(Integer)
    ta = Column(Integer)
    date = Column(Date, primary_key=True)


