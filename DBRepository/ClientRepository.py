from sqlalchemy.exc import IntegrityError
from DBRepository.BaseRepository import BaseRepository
from DBModels.Client import Client

class ClientRepository(BaseRepository):
    def add(self, client: Client):
        try:
            if self.session:
                self.session.add(client)
                self.session.commit()
            else:
                self.clients.append(client)
        except IntegrityError:
            print("IntegrityError: Client already exists in the database.")
            if self.session:
                self.session.rollback()
    
    def remove(self, client_id):
        client = self.session.query(Client).filter_by(id=client_id).one_or_none()
        if client:
            try:
                self.session.delete(client)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Client does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Client with id {client_id} not found.")
    
    def update(self, client: Client):
        client = self.session.query(Client).filter_by(id=client.id).first()
        if client:
            try:
                self.session.merge(client)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Client does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Client with id {client.id} not found.")

    def get_all(self):
        return self.session.query(Client).all()
    
    def get_by_id(self, id):
        client = self.session.query(Client).filter_by(id=id).first()
        if client:
            return client
        else:
            return None