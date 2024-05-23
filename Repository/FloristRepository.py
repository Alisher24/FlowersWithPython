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

    def update(self, florist):
        exists_florist = self.get_by_id(florist.id)
        if exists_florist:
            self.florists.remove(exists_florist)
            self.florists.append(florist)

    def get_all(self):
        return self.florists

    def get_by_id(self, id):
        if self.florists:
            for f in self.florists:
                if f.id == id:
                    return f
        return None