class Client:
    def __init__(self, id: int, name: str, discount: float):
        self.id = id
        self.name = name
        self.discount = discount
    
    def get_info(self):
        return [self.id, self.name, self.discount]
    
    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return (self.id == other.id and
                self.name == other.name and
                self.discount == other.discount)
    