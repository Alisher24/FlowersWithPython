from Repository.XMLRepos.FloristXMLRepository import FloristXMLRepository
from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.Bouquet import Bouquet

class BouquetXMLRepository(FakeRepository):
    def __init__(self, file_path, florist_repository: FloristXMLRepository):
        super().__init__(file_path)
        self.root = self._load_xml()
        self.florist_repository = florist_repository

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
        for bouquet_element in self.root.findall(".//bouquets/bouquet"):
            if int(bouquet_element.find("id").text) == id:
                return self._xml_to_bouquet(bouquet_element)
        return None

    def add(self, bouquet):
        bouquets_element = self.root.find(".//bouquets")
        if bouquets_element is None:
            bouquets_element = ET.SubElement(self.root, "bouquets")
        new_bouquet_element = ET.SubElement(bouquets_element, "bouquet")
        self._bouquet_to_xml(bouquet, new_bouquet_element)
        self._save_xml()

    def remove(self, bouquet):
        bouquet_element = self.root.find(".//bouquets/bouquet[name='{}']".format(bouquet.name))
        if bouquet_element is not None:
            self.root.find(".//bouquets").remove(bouquet_element)
            self._save_xml()

    def update(self, bouquet):
        bouquet_element = self.get_by_id(bouquet.id)
        if bouquet_element is not None:
            self.add(bouquet)
            self.remove(bouquet_element)
            self._save_xml()

    def get_all(self):
        bouquets = []
        for bouquet_element in self.root.findall(".//bouquets/bouquet"):
            bouquets.append(self._xml_to_bouquet(bouquet_element))
        return bouquets

    def _xml_to_bouquet(self, bouquet_element):
        id = int(bouquet_element.find("id").text)
        name = bouquet_element.find("name").text
        price = int(bouquet_element.find("price").text)
        florist = FloristXMLRepository("").get_by_id(int(bouquet_element.find("id").text))
        return Bouquet(id=id, name=name, price=price, florist=florist)

    def _bouquet_to_xml(self, bouquet, bouquet_element):
        id_element = bouquet_element.find("id")
        if id_element is not None:
            id_element.text = bouquet.id
        else:
            id_element = ET.SubElement(bouquet_element, "id")
            id_element.text = str(bouquet.id)
        
        name_element = bouquet_element.find("name")
        if name_element is not None:
            name_element.text = bouquet.name
        else:
            name_element = ET.SubElement(bouquet_element, "name")
            name_element.text = bouquet.name

        price_element = bouquet_element.find("price")
        if price_element is not None:
            price_element.text = bouquet.price
        else:
            price_element = ET.SubElement(bouquet_element, "price")
            price_element.text = str(bouquet.price)

        florist_element = bouquet_element.find("florist")
        if florist_element is not None:
            florist_element.text = str(bouquet.florist)
        else:
            florist_element = ET.SubElement(bouquet_element, "florist")
            florist_element.text = str(bouquet.florist)