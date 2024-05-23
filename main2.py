from Procedures import BouquetProcedure, ClientsProcedure, DeliveryProcedure, FloristsProcedure, FlowersInStockProcedure, FlowersOfProviderProcedure, FlowersProcedure, ProviderProcedure
from Repository import BouquetRepository, ClientsRepository, DeliveryRepository, FloristRepository, FlowerRepository, FlowersInStockRepository, FlowersOfProviderRepository, ProviderRepository
import datetime

ClientUC = ClientsProcedure.ClientProcedure(ClientsRepository.ClientRepository())
FlowerUC = FlowersProcedure.FlowersProcedure(FlowerRepository.FlowerRepository())
FloristUC = FloristsProcedure.FloristsProcedure(FloristRepository.FloristRepository())
BouquetUC = BouquetProcedure.BouquetProcedure(BouquetRepository.BouquetRepository())

ClientUC.add_client(0, "Alisher", 5)
FlowerUC.add_flowers(0, "Rose")
FloristUC.add_florist(0, "Ashot", datetime.date(2002, 11, 1), 10)
BouquetUC.add_bouquet(0, "101 Rose", 5000, FloristUC.get_florist(0))