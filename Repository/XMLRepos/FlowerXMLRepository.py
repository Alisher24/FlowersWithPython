from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.Flowers import Flowers

class FlowerXMLRepository(FakeRepository):
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
        for flower_element in self.root.findall(".//flowers/flower"):
            if flower_element.find("id").text == id:
                return self._xml_to_flower(flower_element)
        return None

    def add(self, flower):
        flowers_element = self.root.find(".//flowers")
        if flowers_element is None:
            flowers_element = ET.SubElement(self.root, "flowers")
        new_flower_element = ET.SubElement(flowers_element, "flower")
        self._flower_to_xml(flower, new_flower_element)
        self._save_xml()

    def remove(self, flower):
        flower_element = self.root.find(".//flowers/flower[name='{}']".format(flower.name))
        if flower_element is not None:
            self.root.find(".//flowers").remove(flower_element)
            self._save_xml()

    def update(self, flower):
        flower_element = self.get_by_id(flower.id)
        if flower_element is not None:
            self.add(flower)
            self.remove(flower_element)
            self._save_xml()

    def get_all(self):
        flowers = []
        for flower_element in self.root.findall(".//flowers/flower"):
            flowers.append(self._xml_to_flower(flower_element))
        return flowers

    def _xml_to_flower(self, flower_element):
        id = int(flower_element.find("id").text)
        name = flower_element.find("name").text
        return Flowers(id=id, name=name)

    def _flower_to_xml(self, flower, flower_element):
        id_element = flower_element.find("id")
        if id_element is not None:
            id_element.text = flower.id
        else:
            id_element = ET.SubElement(flower_element, "id")
            id_element.text = str(flower.id)
        
        name_element = flower_element.find("name")
        if name_element is not None:
            name_element.text = flower.name
        else:
            name_element = ET.SubElement(flower_element, "name")
            name_element.text = flower.name