from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.FlowersInStock import FlowersInStock

class FlowersInStockRepository(BaseRepository):
    def add(self, flowersInStock: FlowersInStock):
        try:
            self.session.add(flowersInStock)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: FlowersInStock already exists in the database.")
            self.session.rollback()
    
    def remove(self, flowersInStock_id):
        flowersInStock = self.session.query(FlowersInStock).filter_by(id=flowersInStock_id).first()
        if flowersInStock:
            try:
                self.session.delete(flowersInStock)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: FlowersInStock does not exist in the database.")
                self.session.rollback()
        else:
            print(f"FlowersInStock with id {flowersInStock_id} not found.")
    
    def update(self, flowersInStock: FlowersInStock):
        flowersInStock = self.session.query(FlowersInStock).filter_by(id=flowersInStock.id).first()
        if flowersInStock:
            try:
                self.session.merge(flowersInStock)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: FlowersInStock does not exist in the database.")
                self.session.rollback()
        else:
            print(f"FlowersInStock with id {flowersInStock.id} not found.")
    
    def get_all(self):
        return self.session.query(FlowersInStock).all()
    
    def get_by_id(self, id):
        flowersInStock = self.session.query(FlowersInStock).filter_by(id=id).first()
        if flowersInStock:
            return flowersInStock
        else:
            return None