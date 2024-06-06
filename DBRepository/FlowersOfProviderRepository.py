from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.FlowersOfProvider import FlowersOfProvider

class FlowersOfProviderRepository(BaseRepository):
    def add(self, flowersOfProvider: FlowersOfProvider):
        try:
            self.session.add(flowersOfProvider)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: FlowersOfProvider already exists in the database.")
            self.session.rollback()
    
    def remove(self, flowersOfProvider_id):
        flowersOfProvider = self.session.query(FlowersOfProvider).filter_by(id=flowersOfProvider_id).first()
        if flowersOfProvider:
            try:
                self.session.delete(flowersOfProvider)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: FlowersOfProvider does not exist in the database.")
                self.session.rollback()
        else:
            print(f"FlowersOfProvider with id {flowersOfProvider_id} not found.")
    
    def update(self, flowersOfProvider: FlowersOfProvider):
        flowersOfProvider = self.session.query(FlowersOfProvider).filter_by(id=flowersOfProvider.id).first()
        if flowersOfProvider:
            try:
                self.session.merge(flowersOfProvider)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: FlowersOfProvider does not exist in the database.")
                self.session.rollback()
        else:
            print(f"FlowersOfProvider with id {flowersOfProvider.id} not found.")
    
    def get_all(self):
        return self.session.query(FlowersOfProvider).all()
    
    def get_by_id(self, id):
        flowersOfProvider = self.session.query(FlowersOfProvider).filter_by(id=id).first()
        if flowersOfProvider:
            return flowersOfProvider
        else:
            return None