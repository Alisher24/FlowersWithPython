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

    def get_all(self):
        return self.clients

    def get_by_id(self, id):
        if self.clients:
            for c in self.clients:
                if c.id == id:
                    return c
        return "Клиент по данному id не найден"