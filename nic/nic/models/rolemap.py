from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class RoleMap(Base):
    __tablename__ = 'role_map'
    role_id = Column(Integer, primary_key=True)
    role_desc = Column(Text)
