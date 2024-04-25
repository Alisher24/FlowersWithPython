from Repository import FakeRepository

class FloristRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.florists = []

    def add(self, florist):
        self.florists.append(florist)

    def remove(self, florist):
        if self.florists:
            for f in self.florists:
                if f.id == florist.id:
                    self.florists.remove(f)

    def get_all(self):
        return self.florists

    def get_by_id(self, id):
        if self.florists:
            for f in self.florists:
                if f.id == id:
                    return f
        return "Флорист по данному id не найден"