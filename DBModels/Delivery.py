from sqlalchemy import Column, Integer, String, DateTime, Boolean
from DBModels.Base import Base

class Delivery(Base):
    __tablename__ = 'deliveries'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    paymentState = Column(Boolean)
    wish = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'paymentState': self.paymentState,
            'wish': self.wish
        }