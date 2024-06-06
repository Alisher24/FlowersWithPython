from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from DBModels.Base import Base

class FlowersOfProvider(Base):
    __tablename__ = 'flowers_of_providers'

    id = Column(Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey('providers.id'), nullable=False)
    flower_id=Column(Integer, ForeignKey('flowers.id'), nullable=False)
    price = Column(Float)
    provider = relationship("Provider", foreign_keys=[provider_id])
    flower = relationship("Flower", foreign_keys=[flower_id])