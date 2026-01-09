import xml.etree.ElementTree as ET
import os

def read_text_file(file_name):
    data = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split("=")
                data[key] = value

    return data


def write_xml_file(data, xml_file_name):
    root = ET.Element("vehicle")

    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)
    tree.write(xml_file_name, encoding="utf-8", xml_declaration=True)


# ---------- MAIN PROGRAM ----------
current_dir = os.path.dirname(os.path.abspath(__file__))
text_file = os.path.join(current_dir, "data.txt")
xml_file = os.path.join(current_dir, "vehicle_data.xml")

vehicle_data = read_text_file(text_file)
write_xml_file(vehicle_data, xml_file)

print("Vehicle data successfully written to XML file")
