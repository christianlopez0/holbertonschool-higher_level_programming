#!/bin/usr/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    result = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for element in root:
        result[element.tag] = element.text
    return result


if __name__ == "__main__":
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    filename = "data.xml"
    
    # Serialize dictionary to XML
    serialize_to_xml(data, filename)
    print(f"Data serialized and saved to '{filename}'")
    
    # Deserialize XML to dictionary
    deserialized_data = deserialize_from_xml(filename)
    print("Deserialized Data:")
    print(deserialized_data)
