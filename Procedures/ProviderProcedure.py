import warnings

from DBModels.Provider import Provider
from Repository import FakeRepository

class ProviderProcedure:
    def __init__(self, provider_repository: FakeRepository):
        self.provider_repository = provider_repository

    def get_provider(self, id: int) -> Provider:
        return self.provider_repository.get_by_id(id)
    
    def add_provider(self, id: int, name: str):
        if self.get_provider(id):
            warnings.warn("Поставщик с данным id уже существует", UserWarning)
        else:
            provider = Provider(id=id, name=name)
            self.provider_repository.add(provider)
    
    def update_provider(self, id: int, name: str):
        provider = self.get_provider(id)
        if provider:
            update_provider = Provider(id=id, name=name)
            self.provider_repository.update(update_provider)
        else:
            warnings.warn("Поставщика с данным id не существует", UserWarning)

    def remove_provider(self, provider_id):
        romove_provider = self.get_provider(provider_id)
        if romove_provider:
            self.provider_repository.remove(provider_id)
        else: 
             warnings.warn("Данного поставщика не существует", UserWarning)
    
    def get_all_provider(self) -> list[Provider]:
        return self.provider_repository.get_all()
