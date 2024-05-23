from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.Delivery import Delivery
from datetime import datetime

class DeliveryXMLRepository(FakeRepository):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileExistsError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root
    
    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    
    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def get_by_id(self, id):
        for delivery_element in self.root.findall(".//deliverys/delivery"):
            if int(delivery_element.find("id").text) == id:
                return self._xml_to_delivery(delivery_element)
        return None

    def add(self, delivery):
        deliverys_element = self.root.find(".//deliverys")
        if deliverys_element is None:
            deliverys_element = ET.SubElement(self.root, "deliverys")
        new_delivery_element = ET.SubElement(deliverys_element, "delivery")
        self._delivery_to_xml(delivery, new_delivery_element)
        self._save_xml()

    def remove(self, delivery):
        delivery_element = self.root.find(".//deliverys/delivery[name='{}']".format(delivery.name))
        if delivery_element is not None:
            self.root.find(".//deliverys").remove(delivery_element)
            self._save_xml()

    def update(self, delivery):
        delivery_element = self.get_by_id(delivery.id)
        if delivery_element is not None:
            self.add(delivery)
            self.remove(delivery_element)
            self._save_xml()

    def get_all(self):
        deliverys = []
        for delivery_element in self.root.findall(".//deliverys/delivery"):
            deliverys.append(self._xml_to_delivery(delivery_element))
        return deliverys

    def _xml_to_delivery(self, delivery_element):
        id = int(delivery_element.find("id").text)
        date = datetime.fromisoformat(delivery_element.find("date").text)
        paymentState = bool(delivery_element.find("discount").text)
        wish = delivery_element.find("wish").text
        return Delivery(id=id, date=date, paymentState=paymentState, wish=wish)

    def _delivery_to_xml(self, delivery, delivery_element):
        id_element = delivery_element.find("id")
        if id_element is not None:
            id_element.text = delivery.id
        else:
            id_element = ET.SubElement(delivery_element, "id")
            id_element.text = str(delivery.id)
        
        date_element = delivery_element.find("date")
        if date_element is not None:
            date_element.text = delivery.date
        else:
            date_element = ET.SubElement(delivery_element, "date")
            date_element.text = str(delivery.date)
        
        paymentState_element = delivery_element.find("paymentState_element")
        if paymentState_element is not None:
            paymentState_element.text = delivery.paymentState_element
        else:
            paymentState_element = ET.SubElement(delivery_element, "paymentState_element")
            paymentState_element.text = str(delivery.paymentState_element)
        
        wish = delivery_element.find("wish")
        if wish is not None:
            wish.text = delivery.wish
        else:
            wish = ET.SubElement(delivery_element, "wish")
            wish.text = str(delivery.wish)