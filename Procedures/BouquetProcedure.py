import warnings

from DBModels.Bouquet import Bouquet
from Repository import FakeRepository
from DBModels import Florist as florist

class BouquetProcedure:
    def __init__(self, bouquetRepository: FakeRepository):
        self.bouquetRepository = bouquetRepository

    def get_bouquet(self, id: int) -> Bouquet:
        return self.bouquetRepository.get_by_id(id)
    
    def add_bouquet(self, id: int, name: str, price: int, florist_id: int):
        if self.get_bouquet(id):
            warnings.warn("Букет с данным id уже существует", UserWarning)
        else:
            bouquet = Bouquet(id=id, name=name, price=price, florist_id=florist_id)
            self.bouquetRepository.add(bouquet)
    
    def update_bouquet(self, id: int, name: str, price: int, florist_id: int):
        bouquet = self.get_bouquet(id)
        if bouquet:
            update_bouquet = Bouquet(id=id, name=name, price=price, florist_id=florist_id)
            self.bouquetRepository.update(update_bouquet)
        else:
            warnings.warn("Букет с данным id не существует", UserWarning)

    def remove_bouquet(self, bouquet_id):
        romove_bouquet = self.get_bouquet(bouquet_id)
        if romove_bouquet:
            self.bouquetRepository.remove(bouquet_id)
        else: 
             warnings.warn("Данный букет не существует", UserWarning)
    
    def get_all_bouquets(self) -> list[Bouquet]:
        return self.bouquetRepository.get_all()
