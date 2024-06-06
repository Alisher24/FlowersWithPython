import warnings
import datetime

from DBModels.Florist import Florist
from Repository import FakeRepository

class FloristsProcedure:
    def __init__(self, florist_repository: FakeRepository):
        self.florist_repository = florist_repository

    def get_florist(self, id: int) -> Florist:
        return self.florist_repository.get_by_id(id)
    
    def add_florist(self, id: int, name: str, birthday: datetime.date, numberOfCollectedBouquets: int):
        if self.get_florist(id):
            warnings.warn("Флорист с данным id уже существует", UserWarning)
        else:
            florist = Florist(id=id, name=name, birthday=birthday, numberOfCollectedBouquets=numberOfCollectedBouquets)
            self.florist_repository.add(florist)
    
    def update_florist(self, id: int, name: str, birthday: datetime.date, numberOfCollectedBouquets: int):
        florist = self.get_florist(id)
        if florist:
            update_florist = Florist(id=id, name=name, birthday=birthday, numberOfCollectedBouquets=numberOfCollectedBouquets)
            self.florist_repository.update(update_florist)
        else:
            warnings.warn("Флориста с данным id не существует", UserWarning)

    def remove_florist(self, florist_id):
        romove_florist = self.get_florist(florist_id)
        if romove_florist:
            self.florist_repository.remove(florist_id)
        else: 
             warnings.warn("Данного флориста не существует", UserWarning)
    
    def get_all_florists(self) -> list[Florist]:
        return self.florist_repository.get_all()
