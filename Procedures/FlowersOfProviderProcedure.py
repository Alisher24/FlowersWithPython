import warnings

from Models.FlowersOfProvider import FlowersOfProvider
from Models.Provider import Provider
from Models.Flowers import Flowers
from Repository import FakeRepository

class FlowersOfProviderProcedure:
    def __init__(self, flowersOfProvider_repository: FakeRepository):
        self.flowersOfProvider_repository = flowersOfProvider_repository

    def get_flowersOfProvider(self, id: int) -> FlowersOfProvider:
        return self.flowersOfProvider_repository.get_by_id(id)
    
    def add_flowersOfProvider(self, id: int, idOfProvider: Provider, flowers: dict[Flowers, tuple[int, float]]):
        if self.get_flowersOfProvider(id):
            warnings.warn("Цветок с данным id уже существует", UserWarning)
        else:
            flowersOfProvider = FlowersOfProvider(id=id, idOfProvider=idOfProvider, flowers=flowers)
            self.flowersOfProvider_repository.add(flowersOfProvider)
    
    def update_flowersOfProvider(self, id: int, idOfProvider: Provider, flowers: dict[Flowers, tuple[int, float]]):
        flowersOfProvider = self.get_flowersOfProvider(id)
        if flowersOfProvider:
            update_flowersOfProvider = FlowersOfProvider(id=id, idOfProvider=idOfProvider, flowers=flowers)
            self.flowersOfProvider_repository.update(update_flowersOfProvider)
        else:
            warnings.warn("Цветка с данным id не существует", UserWarning)

    def remove_flowersOfProvider(self, flowersOfProvider: FlowersOfProvider):
        romove_flowersOfProvider = self.get_flowersOfProvider(flowersOfProvider.id)
        if romove_flowersOfProvider:
            self.flowersOfProvider_repository.remove(romove_flowersOfProvider)
        else: 
             warnings.warn("Данного цветка не существует", UserWarning)
    
    def get_all_flowersOfProvider(self) -> list[FlowersOfProvider]:
        return self.flowersOfProvider_repository.get_all()
