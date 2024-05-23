from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.Provider import Provider

class ProviderXMLRepository(FakeRepository):
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
        for provider_element in self.root.findall(".//providers/provider"):
            if int(provider_element.find("id").text) == id:
                return self._xml_to_provider(provider_element)
        return None

    def add(self, provider):
        providers_element = self.root.find(".//providers")
        if providers_element is None:
            providers_element = ET.SubElement(self.root, "providers")
        new_provider_element = ET.SubElement(providers_element, "provider")
        self._provider_to_xml(provider, new_provider_element)
        self._save_xml()

    def remove(self, provider):
        provider_element = self.root.find(".//providers/provider[name='{}']".format(provider.name))
        if provider_element is not None:
            self.root.find(".//providers").remove(provider_element)
            self._save_xml()

    def update(self, provider):
        provider_element = self.get_by_id(provider.id)
        if provider_element is not None:
            self.add(provider)
            self.remove(provider_element)
            self._save_xml()

    def get_all(self):
        providers = []
        for provider_element in self.root.findall(".//providers/provider"):
            providers.append(self._xml_to_provider(provider_element))
        return providers

    def _xml_to_provider(self, provider_element):
        id = int(provider_element.find("id").text)
        name = provider_element.find("name").text
        return Provider(id=id, name=name)

    def _provider_to_xml(self, provider, provider_element):
        id_element = provider_element.find("id")
        if id_element is not None:
            id_element.text = provider.id
        else:
            id_element = ET.SubElement(provider_element, "id")
            id_element.text = str(provider.id)
        
        name_element = provider_element.find("name")
        if name_element is not None:
            name_element.text = provider.name
        else:
            name_element = ET.SubElement(provider_element, "name")
            name_element.text = provider.name
