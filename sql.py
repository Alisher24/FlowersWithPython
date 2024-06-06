from Procedures import BouquetProcedure, ClientsProcedure, DeliveryProcedure, FloristsProcedure, FlowersInStockProcedure, FlowersOfProviderProcedure, FlowersProcedure, ProviderProcedure
from DBRepository import BouquetRepository, ClientRepository, DeliveryRepository, FloristRepository, FlowerRepository, FlowersInStockRepository, FlowersOfProviderRepository, ProviderRepository
from DBModels import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///mydatabase.db')
Base.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

BouquetRepos = BouquetRepository.BouquetRepository(session)
ClientRepos = ClientRepository.ClientRepository(session)
DeliveryRepos = DeliveryRepository.DeliveryRepository(session)
FloristRepos = FloristRepository.FloristRepository(session)
FlowerRepos = FlowerRepository.FlowerRepository(session)
FlowersInStockRepos = FlowersInStockRepository.FlowersInStockRepository(session)
FlowersOfProviderRepos = FlowersOfProviderRepository.FlowersOfProviderRepository(session)
ProviderRepos = ProviderRepository.ProviderRepository(session)

BouquetUC = BouquetProcedure.BouquetProcedure(BouquetRepos)
ClientUC = ClientsProcedure.ClientProcedure(ClientRepos)
DeliveryUC = DeliveryProcedure.DeliveryProcedure(DeliveryRepos)
FloristUC = FloristsProcedure.FloristsProcedure(FloristRepos)
FlowerUC = FlowersProcedure.FlowersProcedure(FlowerRepos)
FlowersInStockUC = FlowersInStockProcedure.FlowersInStockProcedure(FlowersInStockRepos)
FlowersOfProviderUC = FlowersOfProviderProcedure.FlowersOfProviderProcedure(FlowersOfProviderRepos)
ProviderUC = ProviderProcedure.ProviderProcedure(ProviderRepos)

# ProviderUC.add_provider(1, "Ashot")
# FlowersOfProviderUC.add_flowersOfProvider(1, 1, 1, 100)
# FlowersInStockUC.add_flowersInStock(1, 1, 100, 150, datetime.datetime(2024, 4, 25, 12, 10))
BouquetUC.add_bouquet(6, "51 роза", 10000, 1)