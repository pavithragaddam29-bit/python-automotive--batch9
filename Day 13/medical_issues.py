import os
import xml.etree.ElementTree as ET

def fetch_medical_issues(xml_file): #This function takes an XML file path as input and returns a list of medical issues.
    tree = ET.parse(xml_file) #This line parses the XML file specified by xml_file and creates an ElementTree object.
    root = tree.getroot()#This line gets the root element of the XML document,
    medical_issues = [] #- An empty list is created to store the medical issues.


    for patient in root.findall('patient'): #method is used to find all <patient> elements in the XML tree.
        issue = patient.find('issue').text
        medical_issues.append(issue)

    return sorted(set(medical_issues))  # Remove duplicates and sort

def main():
    xml_file = os.path.join(os.path.dirname(__file__), 'example.xml')
    try:
        medical_issues = fetch_medical_issues(xml_file)
        print("Medical Issues (Alphabetical Order):")
        for issue in medical_issues:
            print(f"- {issue}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
