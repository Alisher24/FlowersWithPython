from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.FlowersInStock import FlowersInStock
from Repository.XMLRepos.FlowerXMLRepository import FlowerXMLRepository
from datetime import datetime

class FlowersInStockXMLRepository(FakeRepository):
    def __init__(self, file_path, flower_repository: FlowerXMLRepository):
        super().__init__(file_path)
        self.root = self._load_xml()
        self.flower_repository = flower_repository

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
        for flowersInStock_element in self.root.findall(".//flowersInStocks/flowersInStock"):
            if int(flowersInStock_element.find("id").text) == id:
                return self._xml_to_flowersInStock(flowersInStock_element)
        return None

    def add(self, flowersInStock):
        flowersInStocks_element = self.root.find(".//flowersInStocks")
        if flowersInStocks_element is None:
            flowersInStocks_element = ET.SubElement(self.root, "flowersInStocks")
        new_flowersInStock_element = ET.SubElement(flowersInStocks_element, "flowersInStock")
        self._flowersInStock_to_xml(flowersInStock, new_flowersInStock_element)
        self._save_xml()

    def remove(self, flowersInStock):
        flowersInStock_element = self.root.find(".//flowersInStocks/flowersInStock[name='{}']".format(flowersInStock.name))
        if flowersInStock_element is not None:
            self.root.find(".//flowersInStocks").remove(flowersInStock_element)
            self._save_xml()

    def update(self, flowersInStock):
        flowersInStock_element = self.get_by_id(flowersInStock.id)
        if flowersInStock_element is not None:
            self.add(flowersInStock)
            self.remove(flowersInStock_element)
            self._save_xml()

    def get_all(self):
        flowersInStocks = []
        for flowersInStock_element in self.root.findall(".//flowersInStocks/flowersInStock"):
            flowersInStocks.append(self._xml_to_flowersInStock(flowersInStock_element))
        return flowersInStocks

    def _xml_to_flowersInStock(self, flowersInStock_element):
        id = int(flowersInStock_element.find("id").text)
        flowers = FlowerXMLRepository("").get_by_id(int(flowersInStock_element.find("id").text))
        count = int(flowersInStock_element.find("count").text)
        unitPrice = float(flowersInStock_element.find("unitPrice").text)
        date = datetime.fromisoformat(flowersInStock_element.find("date").text)
        return FlowersInStock(id=id, flowers=flowers, count=count, unitPrice=unitPrice, date=date)

    def _flowersInStock_to_xml(self, flowersInStock, flowersInStock_element):
        id_element = flowersInStock_element.find("id")
        if id_element is not None:
            id_element.text = flowersInStock.id
        else:
            id_element = ET.SubElement(flowersInStock_element, "id")
            id_element.text = str(flowersInStock.id)
        
        flowers_element = flowersInStock_element.find("flowers")
        if flowers_element is not None:
            flowers_element.text = flowersInStock.flowers
        else:
            flowers_element = ET.SubElement(flowersInStock_element, "flowers")
            flowers_element.text = str(flowersInStock.flowers)
        
        count_element = flowersInStock_element.find("count")
        if count_element is not None:
            count_element.text = flowersInStock.count
        else:
            count_element = ET.SubElement(flowersInStock_element, "count")
            count_element.text = str(flowersInStock.count)
        
        unitPrice_element = flowersInStock_element.find("unitPrice")
        if unitPrice_element is not None:
            unitPrice_element.text = flowersInStock.unitPrice
        else:
            unitPrice_element = ET.SubElement(flowersInStock_element, "unitPrice")
            unitPrice_element.text = str(flowersInStock.unitPrice)
        
        date_element = flowersInStock_element.find("date")
        if date_element is not None:
            date_element.text = flowersInStock.date
        else:
            date_element = ET.SubElement(flowersInStock_element, "date")
            date_element.text = str(flowersInStock.date)        
