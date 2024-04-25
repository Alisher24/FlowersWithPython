import datetime

class Florists:
    def __init__(self, id: int, name: str, birthday: datetime.date, numberOfCollectedBouquets: int):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.numberOfCollectedBouquets = numberOfCollectedBouquets
    
    def get_info(self):
        return [self.id, self.name, self.birthday, self.numberOfCollectedBouquets]    
    
    def __eq__(self, other):
        if not isinstance(other, Florists):
            return False
        return (self.id == other.id and
                self.name == other.name and
                self.birthday == other.birthday and
                self.numberOfCollectedBouquets == other.numberOfCollectedBouquets)