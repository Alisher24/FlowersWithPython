from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.Florists import Florists
from datetime import datetime

class FloristXMLRepository(FakeRepository):
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
        for florist_element in self.root.findall(".//florists/florist"):
            if int(florist_element.find("id").text) == id:
                return self._xml_to_florist(florist_element)
        return None

    def add(self, florist):
        florists_element = self.root.find(".//florists")
        if florists_element is None:
            florists_element = ET.SubElement(self.root, "florists")
        new_florist_element = ET.SubElement(florists_element, "florist")
        self._florist_to_xml(florist, new_florist_element)
        self._save_xml()

    def remove(self, florist):
        florist_element = self.root.find(".//florists/florist[name='{}']".format(florist.name))
        if florist_element is not None:
            self.root.find(".//florists").remove(florist_element)
            self._save_xml()

    def update(self, florist):
        florist_element = self.get_by_id(florist.id)
        if florist_element is not None:
            self.add(florist)
            self.remove(florist_element)
            self._save_xml()

    def get_all(self):
        florists = []
        for florist_element in self.root.findall(".//florists/florist"):
            florists.append(self._xml_to_florist(florist_element))
        return florists

    def _xml_to_florist(self, florist_element):
        id = int(florist_element.find("id").text)
        name = florist_element.find("name").text
        birthday = datetime.fromisoformat(florist_element.find("birthday").text)
        numberOfCollectedBouquets = int(florist_element.find("numberOfCollectedBouquets").text)
        return Florists(id=id, name=name, birthday=birthday, numberOfCollectedBouquets=numberOfCollectedBouquets)

    def _florist_to_xml(self, florist, florist_element):
        id_element = florist_element.find("id")
        if id_element is not None:
            id_element.text = florist.id
        else:
            id_element = ET.SubElement(florist_element, "id")
            id_element.text = str(florist.id)
        
        name_element = florist_element.find("name")
        if name_element is not None:
            name_element.text = florist.name
        else:
            name_element = ET.SubElement(florist_element, "name")
            name_element.text = florist.name

        birthday_element = florist_element.find("birthday")
        if birthday_element is not None:
            birthday_element.text = florist.birthday
        else:
            birthday_element = ET.SubElement(florist_element, "birthday")
            birthday_element.text = str(florist.birthday)

        numberOfCollectedBouquets_element = florist_element.find("numberOfCollectedBouquets")
        if numberOfCollectedBouquets_element is not None:
            numberOfCollectedBouquets_element.text = str(florist.numberOfCollectedBouquets)
        else:
            numberOfCollectedBouquets = ET.SubElement(florist_element, "numberOfCollectedBouquets")
            numberOfCollectedBouquets.text = str(florist.numberOfCollectedBouquets)