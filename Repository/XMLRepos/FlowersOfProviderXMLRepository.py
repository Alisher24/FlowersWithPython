from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.FlowersOfProvider import FlowersOfProvider

class FlowersOfProviderXMLRepository(FakeRepository):
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
        for flowersOfProvider_element in self.root.findall(".//flowersOfProviders/flowersOfProvider"):
            if int(flowersOfProvider_element.find("id").text) == id:
                return self._xml_to_flowersOfProvider(flowersOfProvider_element)
        return None

    def add(self, flowersOfProvider):
        flowersOfProviders_element = self.root.find(".//flowersOfProviders")
        if flowersOfProviders_element is None:
            flowersOfProviders_element = ET.SubElement(self.root, "flowersOfProviders")
        new_flowersOfProvider_element = ET.SubElement(flowersOfProviders_element, "flowersOfProvider")
        self._flowersOfProvider_to_xml(flowersOfProvider, new_flowersOfProvider_element)
        self._save_xml()

    def remove(self, flowersOfProvider):
        flowersOfProvider_element = self.root.find(".//flowersOfProviders/flowersOfProvider[name='{}']".format(flowersOfProvider.name))
        if flowersOfProvider_element is not None:
            self.root.find(".//flowersOfProviders").remove(flowersOfProvider_element)
            self._save_xml()

    def update(self, flowersOfProvider):
        flowersOfProvider_element = self.get_by_id(flowersOfProvider.id)
        if flowersOfProvider_element is not None:
            self.add(flowersOfProvider)
            self.remove(flowersOfProvider_element)
            self._save_xml()

    def get_all(self):
        flowersOfProviders = []
        for flowersOfProvider_element in self.root.findall(".//flowersOfProviders/flowersOfProvider"):
            flowersOfProviders.append(self._xml_to_flowersOfProvider(flowersOfProvider_element))
        return flowersOfProviders

    def _xml_to_flowersOfProvider(self, flowersOfProvider_element):
        id = int(flowersOfProvider_element.find("id").text)
        idOfProvider = int(flowersOfProvider_element.find("idOfProvider").text)
        flowers = dict(flowersOfProvider_element.find("flowers").text)
        return FlowersOfProvider(id=id, idOfProvider=idOfProvider, flowers=flowers)

    def _flowersOfProvider_to_xml(self, flowersOfProvider, flowersOfProvider_element):
        id_element = flowersOfProvider_element.find("id")
        if id_element is not None:
            id_element.text = flowersOfProvider.id
        else:
            id_element = ET.SubElement(flowersOfProvider_element, "id")
            id_element.text = str(flowersOfProvider.id)
        
        idOfProvider_element = flowersOfProvider_element.find("idOfProvider")
        if idOfProvider_element is not None:
            idOfProvider_element.text = flowersOfProvider.idOfProvider
        else:
            idOfProvider_element = ET.SubElement(flowersOfProvider_element, "idOfProvider")
            idOfProvider_element.text = str(flowersOfProvider.idOfProvider)
        
        flowers_element = flowersOfProvider_element.find("flowers")
        if flowers_element is not None:
            flowers_element.text = flowersOfProvider.flowers
        else:
            flowers_element = ET.SubElement(flowersOfProvider_element, "flowers")
            flowers_element.text = str(flowersOfProvider.flowers)