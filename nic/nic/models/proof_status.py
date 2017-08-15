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


class ProofStatus(Base):
    __tablename__ = 'proof_status'
    proof_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey(login.id))
    deduction_id = Column(Text)
    amount = Column(Integer)
    date = Column(Date)
    status = Column(Text)
    count = 0
    
    def proof_generator(self):
        pass
