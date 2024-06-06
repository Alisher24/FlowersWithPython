from sqlalchemy import Column, Integer, String
from DBModels.Base import Base

class Provider(Base):
    __tablename__ = 'providers'

    id = Column(Integer, primary_key=True)
    name = Column(String)