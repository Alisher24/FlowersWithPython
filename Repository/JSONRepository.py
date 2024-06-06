import json
import os
from typing import Type, TypeVar, Generic

T = TypeVar('T')


class JSONRepository(Generic[T]):
    def __init__(self, entity_class: Type[T], file_path: str):
        self.entity_class = entity_class
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def _save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_all(self):
        return [self.entity_class(**item) for item in self.data]

    def get_by_id(self, entity_id):
        for item in self.data:
            if item['id'] == entity_id:
                return self.entity_class(**item)
        return None

    def add(self, entity: T):
        self.data.append(entity.__dict__)
        self._save_data()

    def update(self, entity: T):
        for i, item in enumerate(self.data):
            if item['id'] == entity.id:
                self.data[i] = entity.__dict__
                self._save_data()
                return

    def remove(self, entity_id):
        self.data = [item for item in self.data if item['id'] != entity_id]
        self._save_data()