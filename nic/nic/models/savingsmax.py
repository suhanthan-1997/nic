from sqlalchemy import (
    Column,
    Index,
    Integer,
    ForeignKey,
    Text,
)

from .meta import Base


class savingsMax(Base):
    __tablename__ = 'savings_max'
    year = Column(Integer, primary_key=True)
    c = Column(Integer)
    d1 = Column(Integer)
    d2 = Column(Integer)
    dd = Column(Integer)
    e = Column(Integer)
    u1 = Column(Integer)
    u2 = Column(Integer)
    
    def checkmax(self, stype):
        if stype == 'c':
            a = self.c
        elif stype == 'd1':
            a = self.d1
        elif stype == 'd2':
            a = self.d2
        elif stype == 'dd':
            a = self.dd
        elif stype == 'e':
            a = self.e
        elif stype == 'u1':
            a = self.u1
        else:
            a = self.u2
        return a
