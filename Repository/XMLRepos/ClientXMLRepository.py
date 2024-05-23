from Repository.FakeRepository import FakeRepository
import xml.etree.ElementTree as ET
from Models.Clients import Client

class ClientXMLRepository(FakeRepository):
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
        for client_element in self.root.findall(".//clients/client"):
            if int(client_element.find("id").text) == id:
                return self._xml_to_client(client_element)
        return None

    def add(self, client):
        clients_element = self.root.find(".//clients")
        if clients_element is None:
            clients_element = ET.SubElement(self.root, "clients")
        new_client_element = ET.SubElement(clients_element, "client")
        self._client_to_xml(client, new_client_element)
        self._save_xml()

    def remove(self, client):
        client_element = self.root.find(".//clients/client[name='{}']".format(client.name))
        if client_element is not None:
            self.root.find(".//clients").remove(client_element)
            self._save_xml()

    def update(self, client):
        client_element = self.get_by_id(client.id)
        if client_element is not None:
            self.add(client)
            self.remove(client_element)
            self._save_xml()

    def get_all(self):
        clients = []
        for client_element in self.root.findall(".//clients/client"):
            clients.append(self._xml_to_client(client_element))
        return clients

    def _xml_to_client(self, client_element):
        id = int(client_element.find("id").text)
        name = client_element.find("name").text
        discount = float(client_element.find("discount").text)
        return Client(id=id, name=name, discount=discount)

    def _client_to_xml(self, client, client_element):
        id_element = client_element.find("id")
        if id_element is not None:
            id_element.text = client.id
        else:
            id_element = ET.SubElement(client_element, "id")
            id_element.text = str(client.id)
        
        name_element = client_element.find("name")
        if name_element is not None:
            name_element.text = client.name
        else:
            name_element = ET.SubElement(client_element, "name")
            name_element.text = client.name

        discount_element = client_element.find("discount")
        if discount_element is not None:
            discount_element.text = str(client.discount)
        else:
            discount = ET.SubElement(client_element, "discount")
            discount.text = str(client.discount)