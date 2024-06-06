from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from DBModels.Base import Base

class Bouquet(Base):
    __tablename__ = 'bouquets'

    id = Column(Integer, primary_key=True)
    florist_id = Column(Integer, ForeignKey('florists.id'), nullable=False)
    name = Column(String)
    price = Column(Integer)
    florist = relationship("Florist", foreign_keys=[florist_id])

    def to_dict(self):
        return {
            'id': self.id,
            'florist_id': self.florist_id,
            'name': self.name,
            'price': self.price,
        }