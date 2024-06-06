from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.Bouquet import Bouquet
from DBRepository.FloristRepository import FloristRepository

class BouquetRepository(BaseRepository):
    def add(self, bouquet: Bouquet):
        try:
            self.session.add(bouquet)
            self.session.commit()
            florist = FloristRepository.get_by_id(self, bouquet.florist_id)
            florist.numberOfCollectedBouquets += 1
            FloristRepository.update(self, florist)
        except IntegrityError:
            print("IntegrityError: Bouquet already exists in the database.")
            self.session.rollback()
    
    def remove(self, bouquet_id):
        bouquet = self.session.query(Bouquet).filter_by(id=bouquet_id).first()
        if bouquet:
            try:
                self.session.delete(bouquet)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Bouquet does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Bouquet with id {bouquet_id} not found.")
    
    def update(self, bouquet: Bouquet):
        bouquet = self.session.query(Bouquet).filter_by(id=bouquet.id).first()
        if bouquet:
            try:
                self.session.merge(bouquet)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Bouquet does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Bouquet with id {bouquet.id} not found.")

    def get_all(self):
        return self.session.query(Bouquet).all()
    
    def get_by_id(self, id):
        bouquet = self.session.query(Bouquet).filter_by(id=id).first()
        if bouquet:
            return bouquet
        else:
            return None