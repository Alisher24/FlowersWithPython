class FlowersInStock:
    def __init__(self, id, name, count, unitPrice):
        self.id = id
        self.name = name
        self.count = count
        self.unitPrice = unitPrice

    def get_info(self):
        return [self.id, self.name, self.coun, self.unitPrice]