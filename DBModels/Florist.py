from sqlalchemy import Column, Integer, String, Date
from DBModels.Base import Base

class Florist(Base):
    __tablename__ = 'florists'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)
    numberOfCollectedBouquets = Column(Integer)