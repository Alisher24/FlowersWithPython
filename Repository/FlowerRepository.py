from Repository import FakeRepository

class FlowerRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.flowers = []

    def add(self, flower):
        self.flowers.append(flower)

    def remove(self, flower):
        if self.flowers:
            for f in self.flowers:
                if f.id == flower.id:
                    self.flowers.remove(f)

    def update(self, flower):
        exists_flower = self.get_by_id(flower.id)
        if exists_flower:
            self.flowers.remove(exists_flower)
            self.flowers.append(flower)

    def get_all(self):
        return self.flowers

    def get_by_id(self, id):
        if self.flowers:
            for f in self.flowers:
                if f.id == id:
                    return f
        return None