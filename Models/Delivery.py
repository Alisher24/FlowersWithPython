class Delivery:
    def __init__(self, provider, id, date, paymentState, wish):
        self.id = id
        self.date = date
        self.paymentState = paymentState
        self.wish = wish
        self.provider = provider

    def get_info(self):
        return [self.id, self.date, self.paymentState, self.wish]
    