import warnings

from DBModels.FlowersOfProvider import FlowersOfProvider
from DBModels.Provider import Provider
from DBModels.Flower import Flower
from Repository import FakeRepository

class FlowersOfProviderProcedure:
    def __init__(self, flowersOfProvider_repository: FakeRepository):
        self.flowersOfProvider_repository = flowersOfProvider_repository

    def get_flowersOfProvider(self, id: int) -> FlowersOfProvider:
        return self.flowersOfProvider_repository.get_by_id(id)
    
    def add_flowersOfProvider(self, id: int, provider_id: int, flower_id: int, price: float):
        if self.get_flowersOfProvider(id):
            warnings.warn("Цветок с данным id уже существует", UserWarning)
        else:
            flowersOfProvider = FlowersOfProvider(id=id, provider_id=provider_id, flower_id=flower_id, price=price)
            self.flowersOfProvider_repository.add(flowersOfProvider)
    
    def update_flowersOfProvider(self, id: int, provider_id: int, flower_id: int, price: float):
        flowersOfProvider = self.get_flowersOfProvider(id)
        if flowersOfProvider:
            update_flowersOfProvider = FlowersOfProvider(id=id, provider_id=provider_id, flower_id=flower_id, price=price)
            self.flowersOfProvider_repository.update(update_flowersOfProvider)
        else:
            warnings.warn("Цветка с данным id не существует", UserWarning)

    def remove_flowersOfProvider(self, flowersOfProvider_id):
        romove_flowersOfProvider = self.get_flowersOfProvider(flowersOfProvider_id)
        if romove_flowersOfProvider:
            self.flowersOfProvider_repository.remove(flowersOfProvider_id)
        else: 
             warnings.warn("Данного цветка не существует", UserWarning)
    
    def get_all_flowersOfProvider(self) -> list[FlowersOfProvider]:
        return self.flowersOfProvider_repository.get_all()
