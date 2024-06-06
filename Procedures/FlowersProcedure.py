import warnings

from DBModels.Flower import Flower
from Repository import FakeRepository

class FlowersProcedure:
    def __init__(self, flowers_repository: FakeRepository):
        self.flowers_repository = flowers_repository

    def get_flowers(self, id: int) -> Flower:
        return self.flowers_repository.get_by_id(id)
    
    def add_flowers(self, id: int, name: str):
        if self.get_flowers(id):
            warnings.warn("Цветок с данным id уже существует", UserWarning)
        else:
            flowers = Flower(id=id, name=name)
            self.flowers_repository.add(flowers)
    
    def update_flowers(self, id: int, name: str):
        flowers = self.get_flowers(id)
        if flowers:
            update_flowers = Flower(id=id, name=name)
            self.flowers_repository.update(update_flowers)
        else:
            warnings.warn("Цветока с данным id не существует", UserWarning)

    def remove_flowers(self, flowers_id):
        romove_flowers = self.get_flowers(flowers_id)
        if romove_flowers:
            self.flowers_repository.remove(flowers_id)
        else: 
             warnings.warn("Данного цветока не существует", UserWarning)
    
    def get_all_flowers(self) -> list[Flower]:
        return self.flowers_repository.get_all()
