from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey
)

from .meta import Base
from .rolemap import RoleMap
from .mymodel import login


class UserRoles(Base):
    __tablename__ = 'user_roles'
    rec_id = Column(Integer)
    id = Column(Integer, ForeignKey(login.id), primary_key=True)
    role_id = Column(Integer, ForeignKey(RoleMap.role_id), primary_key=True)
    
