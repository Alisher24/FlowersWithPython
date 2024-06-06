from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class BaseRepository(ABC):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass
