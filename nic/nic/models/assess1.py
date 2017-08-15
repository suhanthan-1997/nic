from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class AssessB(Base):
    __tablename__ = 'assessment_template_b'
    year = Column(Text, primary_key=True)
    slab1 = Column(Integer)
    slab1p = Column(Integer)
    amt1 = Column(Integer)
    slab2 = Column(Integer)
    slab2p = Column(Integer)
    amt2 = Column(Integer)
    slab3 = Column(Integer)
    slab3p = Column(Integer)
    amt3 = Column(Integer)
    
    def calculateTds(self, income, c):
        print('#####')
        print(income)
        red = income - self.slab1
        print(red)
        if income <= self.slab1:
            tax = 0
        elif income in range(self.slab1 + 1, self.slab2):
            tax = 0.1 * red
        elif income in range(self.slab2, self.slab3):
            tax = 0.2 * red + self.amt2
        else:
            tax = 0.3 * red + self.amt3
        print(tax)
        print('####')
        return tax/c
        
        
        
        
