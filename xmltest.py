from Procedures import BouquetProcedure, ClientsProcedure, DeliveryProcedure, FloristsProcedure, FlowersInStockProcedure, FlowersOfProviderProcedure, FlowersProcedure, ProviderProcedure
from Repository.XMLRepos import BouquetXMLRepository, ClientXMLRepository, DeliveryXMLRepository, FloristXMLRepository, FlowersInStockXMLRepository, FlowersOfProviderXMLRepository, FlowerXMLRepository, ProviderXMLRepository
import datetime

file = 'file.xml'

ClientRepos = ClientXMLRepository.ClientXMLRepository(file)
FlowerRepos = FlowerXMLRepository.FlowerXMLRepository(file)
FloristsRepos = FloristXMLRepository.FloristXMLRepository(file)
BouquetRepos = BouquetXMLRepository.BouquetXMLRepository(file, FloristsRepos)

ClientUC = ClientsProcedure.ClientProcedure(ClientRepos)
FlowerUC = FlowersProcedure.FlowersProcedure(FlowerRepos)
FloristUC = FloristsProcedure.FloristsProcedure(FloristsRepos)
BouquetUC = BouquetProcedure.BouquetProcedure(BouquetRepos)

ClientUC.add_client(0, "Alisher", 5)
# FlowerUC.add_flowers(0, "Rose")
# FloristUC.add_florist(0, "Ashot", datetime.date(2002, 11, 1), 10)
# BouquetUC.add_bouquet(0, "101 Rose", 5000, FloristUC.get_florist(0))
