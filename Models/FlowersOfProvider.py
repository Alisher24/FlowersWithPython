from Models import Provider, Flowers

class FlowersOfProvider:
    def __init__(self, id: int, 
                 idOfProvider: Provider.Provider, 
                 flowers: dict[Flowers.Flowers, tuple[int, float]]):
        self.id = id
        self.idOfProvider = idOfProvider
        self.flowers = flowers

    def get_info(self):
        return[self.id, self.idOfProvider, self.flowers]
    
    def __eq__(self, other):
        if not isinstance(other, FlowersOfProvider):
            return False
        return (self.id == other.id and
                self.idOfProvider == other.idOfProvider and
                self.flowers == other.flowers)