import unittest
import BusinessRules
from Models import Delivery, FlowersInStock, Provider
import datetime

class Tests(unittest.TestCase):
    
    def test_check_delivery(self):
        delivery = Delivery(Provider.Provider(1, "Ashot"), 1, datetime.datetime.now() + datetime.timedelta(hours=2), True, "")
        self.assertEqual(BusinessRules.check_delivery(delivery), True)

    def test_check_flowers(self):
        flowers = FlowersInStock.FlowersInStock(1, "Роза", datetime.datetime.now() - datetime.timedelta(days=1), 100)
        self.assertEqual(BusinessRules.check_flowers(flowers), True)

    def test_check_time_delivery(self):
        deliveries = [Delivery(Provider.Provider(1, "Ashot"), 1, datetime.datetime.now() + datetime.timedelta(hours=2), True, "")]
        delivery = Delivery(Provider.Provider(1, "Ashot"), 1, datetime.datetime.now() + datetime.timedelta(hours=2), True, "")
        self.assertEqual(BusinessRules.check_time_delivery(deliveries, delivery), False)

    def test_check_time_flowers(self):
        flowers = [FlowersInStock.FlowersInStock(1, "Роза", datetime.datetime.now() - datetime.timedelta(days=2), 100)]
        self.assertEqual(BusinessRules.check_time_flowers(flowers), True)
    
if __name__ == '__main__':
    unittest.main()