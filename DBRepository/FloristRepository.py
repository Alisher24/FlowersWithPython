from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.Florist import Florist

class FloristRepository(BaseRepository):
    def add(self, florist: Florist):
        try:
            self.session.add(florist)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Florist already exists in the database.")
            self.session.rollback()
    
    def remove(self, florist_id):
        florist = self.session.query(Florist).filter_by(id=florist_id).first()
        if florist:
            try:
                self.session.delete(florist)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Florist does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Florist with id {florist_id} not found.")
    
    def update(self, florist: Florist):
        florist = self.session.query(Florist).filter_by(id=florist.id).first()
        if florist:
            try:
                self.session.merge(florist)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Florist does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Florist with id {florist.id} not found.")
    
    def get_all(self):
        return self.session.query(Florist).all()
    
    def get_by_id(self, id):
        florist = self.session.query(Florist).filter_by(id=id).first()
        if florist:
            return florist
        else:
            return None