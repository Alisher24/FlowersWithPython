import warnings
import datetime

from Models.FlowersInStock import FlowersInStock
from Models.Flowers import Flowers
from Repository import FakeRepository

class FlowersInStockProcedure:
    def __init__(self, flowersInStock_repository: FakeRepository):
        self.flowersInStock_repository = flowersInStock_repository

    def get_flowersInStock(self, id: int) -> FlowersInStock:
        return self.flowersInStock_repository.get_by_id(id)
    
    def add_flowersInStock(self, id: int, flowers: Flowers, count: int, unitPrice: float, date: datetime):
        if self.get_flowersInStock(id):
            warnings.warn("Цветок с данным id уже существует", UserWarning)
        else:
            flowersInStock = FlowersInStock(id=id, flowers=flowers, count=count, unitPrice=unitPrice, date=date)
            self.flowersInStock_repository.add(flowersInStock)
    
    def update_flowersInStock(self, id: int, flowers: Flowers, count: int, unitPrice: float, date: datetime):
        flowersInStock = self.get_flowersInStock(id)
        if flowersInStock:
            update_flowersInStock = FlowersInStock(id=id, flowers=flowers, count=count, unitPrice=unitPrice, date=date)
            self.flowersInStock_repository.update(update_flowersInStock)
        else:
            warnings.warn("Цветок с данным id не существует", UserWarning)

    def remove_flowersInStock(self, flowersInStock: FlowersInStock):
        romove_flowersInStock = self.get_flowersInStock(flowersInStock.id)
        if romove_flowersInStock:
            self.flowersInStock_repository.remove(romove_flowersInStock)
        else: 
             warnings.warn("Данного цветока не существует", UserWarning)
    
    def get_all_flowersInStock(self) -> list[FlowersInStock]:
        return self.flowersInStock_repository.get_all()
