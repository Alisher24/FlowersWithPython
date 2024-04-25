class FlowersOfProvider:
    def __init__(self, id, idOfProvider, flowers):
        self.id = id
        self.idOfProvider = idOfProvider
        self.flowers = flowers

    def get_info(self):
        return[self.id, self.idOfProvider, self.flowers]