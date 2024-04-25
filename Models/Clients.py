class Client:
    def __init__(self, id, name, discount):
        self.id = id
        self.name = name
        self.discount = discount
    
    def get_info(self):
        return [self.id, self.name, self.discount]
    