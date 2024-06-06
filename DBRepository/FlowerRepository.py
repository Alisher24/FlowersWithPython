from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.Flower import Flower

class FlowerRepository(BaseRepository):
    def add(self, flower: Flower):
        try:
            self.session.add(flower)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Flower already exists in the database.")
            self.session.rollback()
    
    def remove(self, flower_id):
        flower = self.session.query(Flower).filter_by(id=flower_id).first()
        if flower:
            try:
                self.session.delete(flower)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Flower does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Flower with id {flower_id} not found.")
    
    def update(self, flower: Flower):
        flower = self.session.query(Flower).filter_by(id=flower.id).first()
        if flower:
            try:
                self.session.merge(flower)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Flower does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Flower with id {flower.id} not found.")
    
    def get_all(self):
        return self.session.query(Flower).all()
    
    def get_by_id(self, id):
        flower = self.session.query(Flower).filter_by(id=id).first()
        if flower:
            return flower
        else:
            return None