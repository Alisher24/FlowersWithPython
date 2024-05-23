from Repository import FakeRepository

class ClientRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.clients = []

    def add(self, client):
        self.clients.append(client)

    def remove(self, client):
        if self.clients:
            for c in self.clients:
                if c.id == client.id:
                    self.clients.remove(c)

    def update(self, client):
        exists_client = self.get_by_id(client.id)
        if exists_client:
            self.clients.remove(exists_client)
            self.clients.append(client)

    def get_all(self):
        return self.clients

    def get_by_id(self, id):
        if self.clients:
            for c in self.clients:
                if c.id == id:
                    return c
        return None