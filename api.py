import requests
import json
import xml.etree.ElementTree as ET

with open('toxins.json', 'r') as f:
    data = json.load(f)
# Si data es una lista, imprime los valores de las claves especificadas para cada diccionario

query_dictionary = {}
if type(data) is list:
    for dic in data:
        chembl_id = dic.get('chembl_id')
        if chembl_id:  # Si chembl_id no es None o vacío
            common_name = dic.get('common_name')
            pubchem_id = dic.get('pubchem_id')
            query_dictionary[common_name] = [pubchem_id, chembl_id]

total_sequences =1457

cid1 = query_dictionary['Benzene'][0]
chembl_id1 = query_dictionary['Benzene'][1]

import requests

def pubchem_requests(cid):
    # Request basic compound information
    basic_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IUPACName,MolecularFormula,CanonicalSMILES,IsomericSMILES,InChIKey,MolecularWeight/JSON"
    basic_response = requests.get(basic_url)
    basic_data = basic_response.json()
    
    if 'Fault' in basic_data:
        print("Error:", basic_data['Fault']['Message'])
        return None
    
    # Extract basic compound information
    properties = basic_data['PropertyTable']['Properties'][0]
    compound_name = properties.get('IUPACName', 'N/A')
    chemical_formula = properties.get('MolecularFormula', 'N/A')
    canonical_smiles = properties.get('CanonicalSMILES', 'N/A')
    isomeric_smiles = properties.get('IsomericSMILES', 'N/A')
    molecular_weight = properties.get('MolecularWeight', 'N/A')
    inchi_key = properties.get('InChIKey', 'N/A')
    
    # Request compound description
    description_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/description/JSON"
    description_response = requests.get(description_url)
    description_data = description_response.json()
    
    if 'Fault' in description_data:
        print("Error:", description_data['Fault']['Message'])
        return None
    
    # Extract compound description
    description = description_data['InformationList']['Information'][1].get('Description', 'N/A')
    
    return compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key, description

# Example usage
compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key, description = pubchem_requests(241)

print("Compound name:", compound_name)
print("Chemical formula:", chemical_formula)
print("Canonical SMILES:", canonical_smiles)
print("Isomeric SMILES:", isomeric_smiles)
print("Molecular weight:", molecular_weight)
print("InChI Key:", inchi_key)
print("Description:", description)


def get_ghs_pictograms(cid):
    # Request GHS classification information
    ghs_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON/?heading=GHS+Classification"
    ghs_response = requests.get(ghs_url)
    ghs_data = ghs_response.json()
    
    if 'Fault' in ghs_data:
        print("Error:", ghs_data['Fault']['Message'])
        return None
    
    # Navigate to the section containing GHS Classification
    sections = ghs_data['Record']['Section']
    for section in sections:
        if section.get('TOCHeading') == 'Safety and Hazards':
            hazards_section = section.get('Section')
            for sub_section in hazards_section:
                if sub_section.get('TOCHeading') == 'Hazards Identification':
                    ghs_classification_section = sub_section.get('Section')
                    for sub_sub_section in ghs_classification_section:
                        if sub_sub_section.get('TOCHeading') == 'GHS Classification':
                            pictograms_info = sub_sub_section.get('Information')
                            pictogram_urls = set()  # Use a set to collect unique URLs
                            for info in pictograms_info:
                                if info.get('Name') == 'Pictogram(s)':
                                    pictograms_markup = info.get('Value', {}).get('StringWithMarkup', [])
                                    for markup in pictograms_markup:
                                        pictogram_url = markup.get('Markup')[0].get('URL')
                                        pictogram_urls.add(pictogram_url)  # Add URL to the set
                            return list(pictogram_urls)  # Convert set back to a list
    return None


# Example usage
pictogram_urls = get_ghs_pictograms(241)
print(pictogram_urls)











