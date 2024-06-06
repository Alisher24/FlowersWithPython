from flask import Flask, jsonify, request
from Repository.UnitOfWork import UnitOfWork
from DBModels import Base, Bouquet, Client, Delivery, Florist, Flower, FlowersInStock, FlowersOfProvider, Provider
from DBRepository import BouquetRepository, ClientRepository, DeliveryRepository, FloristRepository, FlowerRepository, FlowersInStockRepository, FlowersOfProviderRepository, ProviderRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///mydatabase.db')
Base.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Создаем Unit of Work
uow = UnitOfWork('sqlite:///mydatabase.db')

# Создаем репозиторий для клиентов
client_repo = ClientRepository.ClientRepository(session)
florist_repo = FloristRepository.FloristRepository(session)
flower_repo = FlowerRepository.FlowerRepository(session)
provider_repo = ProviderRepository.ProviderRepository(session)
delivery_repo = DeliveryRepository.DeliveryRepository(session)
bouquet_repo = BouquetRepository.BouquetRepository(session)
flowers_in_stock_repo = FlowersInStockRepository.FlowersInStockRepository(session)
flowers_of_provider_repo = FlowersOfProviderRepository.FlowersOfProviderRepository(session)

# Для клиента
@app.route('/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    new_client = Client.Client(**data)
    with uow:
        client_repo.add(new_client)
    return jsonify({'message': 'Client created successfully'}), 201

@app.route('/clients', methods=['GET'])
def get_clients():
    with uow:
        clients = client_repo.get_all()
    return jsonify([client.to_dict() for client in clients]), 200

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    with uow:
        client = client_repo.get_by_id(client_id)
    if client:
        return jsonify(client.to_dict()), 200
    return jsonify({'message': 'Client not found'}), 404

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    with uow:
        client = client_repo.get_by_id(client_id)
        if client:
            for key, value in data.items():
                setattr(client, key, value)
            client_repo.update(client)
            return jsonify({'message': 'Client updated successfully'}), 200
    return jsonify({'message': 'Client not found'}), 404

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    with uow:
        client = client_repo.get_by_id(client_id)
        if client:
            client_repo.remove(client_id)
            return jsonify({'message': 'Client deleted successfully'}), 200
    return jsonify({'message': 'Client not found'}), 404

# Для флориста
@app.route('/florists', methods=['POST'])
def create_florist():
    data = request.get_json()
    new_florist = Florist.Florist(**data)
    with uow:
        florist_repo.add(new_florist)
    return jsonify({'message': 'florist created successfully'}), 201

@app.route('/florists', methods=['GET'])
def get_florists():
    with uow:
        florists = florist_repo.get_all()
    return jsonify([florist.to_dict() for florist in florists]), 200

@app.route('/florists/<int:florist_id>', methods=['GET'])
def get_florist(florist_id):
    with uow:
        florist = florist_repo.get_by_id(florist_id)
    if florist:
        return jsonify(florist.to_dict()), 200
    return jsonify({'message': 'florist not found'}), 404

@app.route('/florists/<int:florist_id>', methods=['PUT'])
def update_florist(florist_id):
    data = request.get_json()
    with uow:
        florist = florist_repo.get_by_id(florist_id)
        if florist:
            for key, value in data.items():
                setattr(florist, key, value)
            florist_repo.update(florist)
            return jsonify({'message': 'florist updated successfully'}), 200
    return jsonify({'message': 'florist not found'}), 404

@app.route('/florists/<int:florist_id>', methods=['DELETE'])
def delete_florist(florist_id):
    with uow:
        florist = florist_repo.get_by_id(florist_id)
        if florist:
            florist_repo.remove(florist_id)
            return jsonify({'message': 'florist deleted successfully'}), 200
    return jsonify({'message': 'florist not found'}), 404

# Для цветов
@app.route('/flowers', methods=['POST'])
def create_flower():
    data = request.get_json()
    new_flower = Flower.Flower(**data)
    with uow:
        flower_repo.add(new_flower)
    return jsonify({'message': 'flower created successfully'}), 201

@app.route('/flowers', methods=['GET'])
def get_flowers():
    with uow:
        flowers = flower_repo.get_all()
    return jsonify([flower.to_dict() for flower in flowers]), 200

@app.route('/flowers/<int:flower_id>', methods=['GET'])
def get_flower(flower_id):
    with uow:
        flower = flower_repo.get_by_id(flower_id)
    if flower:
        return jsonify(flower.to_dict()), 200
    return jsonify({'message': 'flower not found'}), 404

@app.route('/flowers/<int:flower_id>', methods=['PUT'])
def update_flower(flower_id):
    data = request.get_json()
    with uow:
        flower = flower_repo.get_by_id(flower_id)
        if flower:
            for key, value in data.items():
                setattr(flower, key, value)
            flower_repo.update(flower)
            return jsonify({'message': 'flower updated successfully'}), 200
    return jsonify({'message': 'flower not found'}), 404

@app.route('/flowers/<int:flower_id>', methods=['DELETE'])
def delete_flower(flower_id):
    with uow:
        flower = flower_repo.get_by_id(flower_id)
        if flower:
            flower_repo.remove(flower_id)
            return jsonify({'message': 'flower deleted successfully'}), 200
    return jsonify({'message': 'flower not found'}), 404

# Для поставщиков
@app.route('/providers', methods=['POST'])
def create_provider():
    data = request.get_json()
    new_provider = Provider.Provider(**data)
    with uow:
        provider_repo.add(new_provider)
    return jsonify({'message': 'provider created successfully'}), 201

@app.route('/providers', methods=['GET'])
def get_providers():
    with uow:
        providers = provider_repo.get_all()
    return jsonify([provider.to_dict() for provider in providers]), 200

@app.route('/providers/<int:provider_id>', methods=['GET'])
def get_provider(provider_id):
    with uow:
        provider = provider_repo.get_by_id(provider_id)
    if provider:
        return jsonify(provider.to_dict()), 200
    return jsonify({'message': 'provider not found'}), 404

@app.route('/providers/<int:provider_id>', methods=['PUT'])
def update_provider(provider_id):
    data = request.get_json()
    with uow:
        provider = provider_repo.get_by_id(provider_id)
        if provider:
            for key, value in data.items():
                setattr(provider, key, value)
            provider_repo.update(provider)
            return jsonify({'message': 'provider updated successfully'}), 200
    return jsonify({'message': 'provider not found'}), 404

@app.route('/providers/<int:provider_id>', methods=['DELETE'])
def delete_provider(provider_id):
    with uow:
        provider = provider_repo.get_by_id(provider_id)
        if provider:
            provider_repo.remove(provider_id)
            return jsonify({'message': 'provider deleted successfully'}), 200
    return jsonify({'message': 'provider not found'}), 404

# Для доставки
@app.route('/deliverys', methods=['POST'])
def create_delivery():
    data = request.get_json()
    new_delivery = Delivery.Delivery(**data)
    with uow:
        delivery_repo.add(new_delivery)
    return jsonify({'message': 'delivery created successfully'}), 201

@app.route('/deliverys', methods=['GET'])
def get_deliverys():
    with uow:
        deliverys = delivery_repo.get_all()
    return jsonify([delivery.to_dict() for delivery in deliverys]), 200

@app.route('/deliverys/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id):
    with uow:
        delivery = delivery_repo.get_by_id(delivery_id)
    if delivery:
        return jsonify(delivery.to_dict()), 200
    return jsonify({'message': 'delivery not found'}), 404

@app.route('/deliverys/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id):
    data = request.get_json()
    with uow:
        delivery = delivery_repo.get_by_id(delivery_id)
        if delivery:
            for key, value in data.items():
                setattr(delivery, key, value)
            delivery_repo.update(delivery)
            return jsonify({'message': 'delivery updated successfully'}), 200
    return jsonify({'message': 'delivery not found'}), 404

@app.route('/deliverys/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id):
    with uow:
        delivery = delivery_repo.get_by_id(delivery_id)
        if delivery:
            delivery_repo.remove(delivery_id)
            return jsonify({'message': 'delivery deleted successfully'}), 200
    return jsonify({'message': 'delivery not found'}), 404

# Для букета
@app.route('/bouquets', methods=['POST'])
def create_bouquet():
    data = request.get_json()
    new_bouquet = Bouquet.Bouquet(**data)
    with uow:
        bouquet_repo.add(new_bouquet)
    return jsonify({'message': 'bouquet created successfully'}), 201

@app.route('/bouquets', methods=['GET'])
def get_bouquets():
    with uow:
        bouquets = bouquet_repo.get_all()
    return jsonify([bouquet.to_dict() for bouquet in bouquets]), 200

@app.route('/bouquets/<int:bouquet_id>', methods=['GET'])
def get_bouquet(bouquet_id):
    with uow:
        bouquet = bouquet_repo.get_by_id(bouquet_id)
    if bouquet:
        return jsonify(bouquet.to_dict()), 200
    return jsonify({'message': 'bouquet not found'}), 404

@app.route('/bouquets/<int:bouquet_id>', methods=['PUT'])
def update_bouquet(bouquet_id):
    data = request.get_json()
    with uow:
        bouquet = bouquet_repo.get_by_id(bouquet_id)
        if bouquet:
            for key, value in data.items():
                setattr(bouquet, key, value)
            bouquet_repo.update(bouquet)
            return jsonify({'message': 'bouquet updated successfully'}), 200
    return jsonify({'message': 'bouquet not found'}), 404

@app.route('/bouquets/<int:bouquet_id>', methods=['DELETE'])
def delete_bouquet(bouquet_id):
    with uow:
        bouquet = bouquet_repo.get_by_id(bouquet_id)
        if bouquet:
            bouquet_repo.remove(bouquet_id)
            return jsonify({'message': 'bouquet deleted successfully'}), 200
    return jsonify({'message': 'bouquet not found'}), 404

# Для цветов в магазине
@app.route('/flowers_in_stocks', methods=['POST'])
def create_flowers_in_stock():
    data = request.get_json()
    new_flowers_in_stock = FlowersInStock.FlowersInStock(**data)
    with uow:
        flowers_in_stock_repo.add(new_flowers_in_stock)
    return jsonify({'message': 'flowers_in_stock created successfully'}), 201

@app.route('/flowers_in_stocks', methods=['GET'])
def get_flowers_in_stocks():
    with uow:
        flowers_in_stocks = flowers_in_stock_repo.get_all()
    return jsonify([flowers_in_stock.to_dict() for flowers_in_stock in flowers_in_stocks]), 200

@app.route('/flowers_in_stocks/<int:flowers_in_stock_id>', methods=['GET'])
def get_flowers_in_stock(flowers_in_stock_id):
    with uow:
        flowers_in_stock = flowers_in_stock_repo.get_by_id(flowers_in_stock_id)
    if flowers_in_stock:
        return jsonify(flowers_in_stock.to_dict()), 200
    return jsonify({'message': 'flowers_in_stock not found'}), 404

@app.route('/flowers_in_stocks/<int:flowers_in_stock_id>', methods=['PUT'])
def update_flowers_in_stock(flowers_in_stock_id):
    data = request.get_json()
    with uow:
        flowers_in_stock = flowers_in_stock_repo.get_by_id(flowers_in_stock_id)
        if flowers_in_stock:
            for key, value in data.items():
                setattr(flowers_in_stock, key, value)
            flowers_in_stock_repo.update(flowers_in_stock)
            return jsonify({'message': 'flowers_in_stock updated successfully'}), 200
    return jsonify({'message': 'flowers_in_stock not found'}), 404

@app.route('/flowers_in_stocks/<int:flowers_in_stock_id>', methods=['DELETE'])
def delete_flowers_in_stock(flowers_in_stock_id):
    with uow:
        flowers_in_stock = flowers_in_stock_repo.get_by_id(flowers_in_stock_id)
        if flowers_in_stock:
            flowers_in_stock_repo.remove(flowers_in_stock_id)
            return jsonify({'message': 'flowers_in_stock deleted successfully'}), 200
    return jsonify({'message': 'flowers_in_stock not found'}), 404

# Для цветов поставщика
@app.route('/flowers_of_providers', methods=['POST'])
def create_flowers_of_provider():
    data = request.get_json()
    new_flowers_of_provider = FlowersOfProvider.FlowersOfProvider(**data)
    with uow:
        flowers_of_provider_repo.add(new_flowers_of_provider)
    return jsonify({'message': 'flowers_of_provider created successfully'}), 201

@app.route('/flowers_of_providers', methods=['GET'])
def get_flowers_of_providers():
    with uow:
        flowers_of_providers = flowers_of_provider_repo.get_all()
    return jsonify([flowers_of_provider.to_dict() for flowers_of_provider in flowers_of_providers]), 200

@app.route('/flowers_of_providers/<int:flowers_of_provider_id>', methods=['GET'])
def get_flowers_of_provider(flowers_of_provider_id):
    with uow:
        flowers_of_provider = flowers_of_provider_repo.get_by_id(flowers_of_provider_id)
    if flowers_of_provider:
        return jsonify(flowers_of_provider.to_dict()), 200
    return jsonify({'message': 'flowers_of_provider not found'}), 404

@app.route('/flowers_of_providers/<int:flowers_of_provider_id>', methods=['PUT'])
def update_flowers_of_provider(flowers_of_provider_id):
    data = request.get_json()
    with uow:
        flowers_of_provider = flowers_of_provider_repo.get_by_id(flowers_of_provider_id)
        if flowers_of_provider:
            for key, value in data.items():
                setattr(flowers_of_provider, key, value)
            flowers_of_provider_repo.update(flowers_of_provider)
            return jsonify({'message': 'flowers_of_provider updated successfully'}), 200
    return jsonify({'message': 'flowers_of_provider not found'}), 404

@app.route('/flowers_of_providers/<int:flowers_of_provider_id>', methods=['DELETE'])
def delete_flowers_of_provider(flowers_of_provider_id):
    with uow:
        flowers_of_provider = flowers_of_provider_repo.get_by_id(flowers_of_provider_id)
        if flowers_of_provider:
            flowers_of_provider_repo.remove(flowers_of_provider_id)
            return jsonify({'message': 'flowers_of_provider deleted successfully'}), 200
    return jsonify({'message': 'flowers_of_provider not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)