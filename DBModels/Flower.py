from sqlalchemy import Column, Integer, String
from DBModels.Base import Base

class Flower(Base):
    __tablename__ = 'flowers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }