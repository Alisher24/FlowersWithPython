import warnings
import datetime

from Models.Delivery import Delivery
from Repository import FakeRepository

class DeliveryProcedure:
    def __init__(self, delivery_repository: FakeRepository):
        self.delivery_repository = delivery_repository

    def get_delivery(self, id: int) -> Delivery:
        return self.delivery_repository.get_by_id(id)
    
    def add_delivery(self, id: int, date: datetime.datetime, paymentState: bool, wish: str):
        if self.get_delivery(id):
            warnings.warn("Доставка с данным id уже существует", UserWarning)
        else:
            delivery = Delivery(id=id, date=date, paymentState=paymentState, wish=wish)
            self.delivery_repository.add(delivery)
    
    def update_delivery(self, id: int, date: datetime.datetime, paymentState: bool, wish: str):
        delivery = self.get_delivery(id)
        if delivery:
            update_delivery = Delivery(id=id, date=date, paymentState=paymentState, wish=wish)
            self.delivery_repository.update(update_delivery)
        else:
            warnings.warn("Доставка с данным id не существует", UserWarning)

    def remove_delivery(self, delivery: Delivery):
        romove_delivery = self.get_delivery(delivery.id)
        if romove_delivery:
            self.delivery_repository.remove(romove_delivery)
        else: 
             warnings.warn("Данной доставки не существует", UserWarning)
    
    def get_all_deliveries(self) -> list[Delivery]:
        return self.delivery_repository.get_all()
