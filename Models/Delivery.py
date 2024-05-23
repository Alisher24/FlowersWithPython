import datetime

class Delivery:
    def __init__(self, id: int, date: datetime.datetime, paymentState: bool, wish: str):
        self.id = id
        self.date = date
        self.paymentState = paymentState
        self.wish = wish

    def get_info(self):
        return [self.id, self.date, self.paymentState, self.wish]
    
    def __eq__(self, other):
        if not isinstance(other, Delivery):
            return False
        return (self.id == other.id and
                self.date == other.date and
                self.paymentState == other.paymentState and
                self.wish == other.wish)
    