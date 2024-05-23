from Repository import FakeRepository

class ProviderRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.providers = []

    def add(self, provider):
        self.providers.append(provider)

    def remove(self, provider):
        if self.providers:
            for p in self.providers:
                if p.id == provider.id:
                    self.providers.remove(p)

    def update(self, provider):
        exists_provider = self.get_by_id(provider.id)
        if exists_provider:
            self.providers.remove(exists_provider)
            self.providers.append(provider)

    def get_all(self):
        return self.providers

    def get_by_id(self, id):
        if self.providers:
            for p in self.providers:
                if p.id == id:
                    return p
        return None