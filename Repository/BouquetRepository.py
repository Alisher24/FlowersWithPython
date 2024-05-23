from Repository import FakeRepository as fakeRepository
class BouquetRepository(fakeRepository.FakeRepository):

    def __init__(self):
        self.bouquets = []

    def add(self, bouquet):
        self.bouquets.append(bouquet)

    def remove(self, bouquet):
        if self.bouquets:
            for b in self.bouquets:
                if b.id == bouquet.id:
                    self.bouquets.remove(b)

    def update(self, bouquet):
        exists_bouquet = self.get_by_id(bouquet.id)
        if exists_bouquet:
            self.bouquets.remove(exists_bouquet)
            self.bouquets.append(bouquet)

    def get_all(self):
        return self.bouquets

    def get_by_id(self, id):
        if self.bouquets:
            for b in self.bouquets:
                if b.id == id:
                    return b
        return None