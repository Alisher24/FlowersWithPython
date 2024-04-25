class Florists:
    def __init__(self, id, name, birthday, numberOfCollectedBouquets):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.numberOfCollectedBouquets = numberOfCollectedBouquets
    
    def get_info(self):
        return [self.id, self.name, self.birthday, self.numberOfCollectedBouquets]    
    