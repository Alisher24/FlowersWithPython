from Repository import FakeRepository

class DeliveryRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.allDelivery = []

    def add(self, delivery):
        self.allDelivery.append(delivery)

    def remove(self, delivery):
        if self.allDelivery:
            for d in self.allDelivery:
                if d.id == delivery.id:
                    self.allDelivery.remove(d)

    def update(self, delivery):
        exists_delivery = self.get_by_id(delivery.id)
        if exists_delivery:
            self.allDelivery.remove(exists_delivery)
            self.allDelivery.append(delivery)

    def get_all(self):
        return self.allDelivery

    def get_by_id(self, id):
        if self.allDelivery:
            for d in self.allDelivery:
                if d.id == id:
                    return d
        return None