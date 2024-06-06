import warnings

from DBModels.Client import Client
from DBRepository.BaseRepository import BaseRepository

class ClientProcedure:
    def __init__(self, client_repository: BaseRepository):
        self.client_repository = client_repository

    def get_client(self, id: int) -> Client:
        return self.client_repository.get_by_id(id)
    
    def add_client(self, id: int, name: str, discount: int):
        if self.get_client(id):
            warnings.warn("Клиент с данным id уже существует", UserWarning)
        else:
            client = Client(id=id, name=name, discount=discount)
            self.client_repository.add(client)
    
    def update_client(self, id: int, name: str, discount: int):
        client = self.get_client(id)
        if client:
            update_client = Client(id=id, name=name, discount=discount)
            self.client_repository.update(update_client)
        else:
            warnings.warn("Клиент с данным id не существует", UserWarning)

    def remove_client(self, client_id):
        romove_client = self.get_client(client_id)
        if romove_client:
            self.client_repository.remove(client_id)
        else: 
             warnings.warn("Данный клиент не существует", UserWarning)
    
    def get_all_clients(self) -> list[Client]:
        return self.client_repository.get_all()
