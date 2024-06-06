from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from DBModels.Base import Base

class FlowersInStock(Base):
    __tablename__ = 'flowers_in_stocks'

    id = Column(Integer, primary_key=True)
    flower_id = Column(Integer, ForeignKey('flowers.id'), nullable=False)
    count = Column(Integer)
    unitPrice = Column(Float)
    date = Column(DateTime)
    flower = relationship("Flower", foreign_keys=[flower_id])