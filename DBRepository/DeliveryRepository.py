from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.Delivery import Delivery

class DeliveryRepository(BaseRepository):
    def add(self, delivery: Delivery):
        try:
            self.session.add(delivery)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Delivery already exists in the database.")
            self.session.rollback()
    
    def remove(self, delivery_id):
        delivery = self.session.query(Delivery).filter_by(id=delivery_id).first()
        if delivery:
            try:
                self.session.delete(delivery)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Delivery does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Delivery with id {delivery_id} not found.")
    
    def update(self, delivery: Delivery):
        delivery = self.session.query(Delivery).filter_by(id=delivery.id).first()
        if delivery:
            try:
                self.session.merge(delivery)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Delivery does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Delivery with id {delivery.id} not found.")
        
    def get_all(self):
        return self.session.query(Delivery).all()
    
    def get_by_id(self, id):
        delivery = self.session.query(Delivery).filter_by(id=id).first()
        if delivery:
            return delivery
        else:
            return None