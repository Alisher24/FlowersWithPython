from Models import Clients as client, Bouquet as bouquet, Delivery as delivery, Florists as florist, Flowers as flower, FlowersInStock as flowerInStock, FlowersOfProvider as flowersOfProvider, Provider as provider
import datetime
from Repository import BouquetRepository as bouquetRepository, ClientsRepository as clientsRepository

client1 = client.Client(1, "Alisher", 5)
client2 = client.Client(2, "Iliya", 4)
client3 = client.Client(3, "Ashot", 10)

flower1 = flower.Flowers(1, "Роза")
flower2 = flower.Flowers(2, "Лилия")
flower3 = flower.Flowers(3, "Ромашка")
flower4 = flower.Flowers(4, "Пионы")
flower5 = flower.Flowers(5, "Гортензия")

flowerInStock1 = flowerInStock.FlowersInStock(1, flower1, 100, 100)
flowerInStock2 = flowerInStock.FlowersInStock(2, flower2, 100, 100)
flowerInStock3 = flowerInStock.FlowersInStock(3, flower3, 100, 100)

provider1 = provider.Provider(1, "Ashot")
provider2 = provider.Provider(2, "Pashot")
provider3 = provider.Provider(3, "Andrey")

flowersOfProvider1 = flowersOfProvider.FlowersOfProvider(1, 1, {flower1: [1000, 50], flower2: [5000, 50], flower3: [10000, 50]})
flowersOfProvider2 = flowersOfProvider.FlowersOfProvider(2, 2, {flower1: [1000, 60], flower2: [5000, 60], flower3: [10000, 60]})
flowersOfProvider3 = flowersOfProvider.FlowersOfProvider(3, 3, {flower1: [1000, 70], flower2: [5000, 70], flower3: [10000, 70]})

florist1 = florist.Florists(1, "Masha", datetime.date(2002, 11, 1), 10)
florist2 = florist.Florists(2, "Sasha", datetime.date(2002, 11, 1), 10)

bouquet1 = bouquet.Bouquet(1, "51 роза", flowerInStock1.unitPrice * 51)
bouquet2 = bouquet.Bouquet(2, "51 лилия", flowerInStock2.unitPrice * 51)
bouquet3 = bouquet.Bouquet(3, "51 ромашка", flowerInStock3.unitPrice * 51)

delivery1 = delivery.Delivery(provider1, 1, datetime.datetime(2024, 4, 26, 12, 30), True, "")
delivery1 = delivery.Delivery(provider2, 2, datetime.datetime(2024, 4, 26, 13, 30), True, "Сделать фотов")

bouquetRep = bouquetRepository.BouquetRepository()
clientRep = clientsRepository.ClientRepository()

bouquetRep.add(bouquet1)
bouquetRep.add(bouquet2)
bouquetRep.add(bouquet3)

clientRep.add(client1)
clientRep.add(client2)
clientRep.add(client3)

for b in bouquetRep.get_all():
    print(f'Название: {b.name} \nЦена: {b.price} \n')

for c in clientRep.get_all():
    print(f'Имя: {c.name} \nСкидка: {c.discount}% \n')

print('-----------------------------------\n')
bouquetRep.remove(bouquet1)
for b in bouquetRep.get_all():
    print(f'Название: {b.name} \nЦена: {b.price} \n')