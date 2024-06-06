from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.Provider import Provider

class ProviderRepository(BaseRepository):
    def add(self, provider: Provider):
        try:
            self.session.add(provider)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Provider already exists in the database.")
            self.session.rollback()
    
    def remove(self, provider_id):
        provider = self.session.query(Provider).filter_by(id=provider_id).first()
        if provider:
            try:
                self.session.delete(provider)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Provider does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Provider with id {provider_id} not found.")
    
    def update(self, provider: Provider):
        provider = self.session.query(Provider).filter_by(id=provider.id).first()
        if provider:
            try:
                self.session.merge(provider)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Provider does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Provider with id {provider.id} not found.")

    def get_all(self):
        return self.session.query(Provider).all()
    
    def get_by_id(self, id):
        provider = self.session.query(Provider).filter_by(id=id).first()
        if provider:
            return provider
        else:
            return None