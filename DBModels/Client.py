from sqlalchemy import Column, Integer, String, Float
from DBModels.Base import Base

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discount = Column(Float)