from Models import Flowers
import datetime

class FlowersInStock:
    def __init__(self, id: int, flowers: Flowers.Flowers, count: int, unitPrice: float, date: datetime):
        self.id = id
        self.flowers = flowers
        self.count = count
        self.unitPrice = unitPrice
        self.date = date

    def get_info(self):
        return [self.id, self.flowers, self.count, self.unitPrice, self.date]
    
    def __eq__(self, other):
        if not isinstance(other, FlowersInStock):
            return False
        return (self.id == other.id and
                self.flowers == other.flowers and 
                self.count == other.count and
                self.unitPrice == other.unitPrice and
                self.date == other.date)