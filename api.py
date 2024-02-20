import requests
import json
import xml.etree.ElementTree as ET

with open('toxins.json', 'r') as f:
    data = json.load(f)
# Si data es una lista, imprime los valores de las claves especificadas para cada diccionario

query_dictionary = {}
if type(data) is list:
    for dic in data:
        pubchem_id = dic.get('pubchem_id')
        chembl_id = dic.get('chembl_id')
        if pubchem_id and chembl_id:  # If chembl_id and pubchem_id are not None or empty
            common_name = dic.get('common_name')
            types = dic.get('types', [])  # Get the list of types
            type_names = [t.get('type_name') for t in types]  # Extract type_names from the list of types
            mechanism_of_toxicity = dic.get('mechanism_of_toxicity')
            description1 = dic.get('description')
            metabolism = dic.get('metabolism')
            toxicity = dic.get('toxicity')
            lethaldose = dic.get('lethaldose')
            symptoms = dic.get('symptoms')
            treatment = dic.get('treatment')
            health_effects = dic.get('health_effects')

            query_dictionary[common_name] = [pubchem_id, chembl_id, type_names, mechanism_of_toxicity, description1, toxicity, symptoms, treatment, health_effects]

def get_compound_data(query_dictionary, compound_name):
    return query_dictionary.get(compound_name)

# Example usage:
compound_data = get_compound_data(query_dictionary, 'Benzene')
'''
if compound_data:
    pubchem_id, chembl_id, type_names, mechanism_of_toxicity, description1, toxicity, symptoms, treatment, health_effects = compound_data
    print("PubChem ID:", pubchem_id)
    print("ChEMBL ID:", chembl_id)
    print("Type Names:", type_names)
    print("Mechanism of Toxicity:", mechanism_of_toxicity)
    print("Description:", description1)
    print("Metabolism:", metabolism)
    print("Toxicity:", toxicity)
    print("Lethal Dose:", lethaldose)
    print("Symptoms:", symptoms)
    print("Treatment:", treatment)
    print("Health Effects:", health_effects)
else:
    print("Compound not found in the query dictionary.")
    
'''

identifiers = "tox{number}"
cid1 = query_dictionary['Benzene'][0]
chembl_id1 = query_dictionary['Benzene'][1]

for key, value in query_dictionary.items():
    cid = query_dictionary[key][0]


def pubchem_requests(cid):
    try:
        # Request basic compound information
        basic_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IUPACName,MolecularFormula,CanonicalSMILES,IsomericSMILES,InChIKey,MolecularWeight/JSON"
        basic_response = requests.get(basic_url)
        basic_data = basic_response.json()
        
        if 'Fault' in basic_data:
            print("Error in basic information request:", basic_data['Fault']['Message'])
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
        
        if 'InformationList' in description_data and 'Information' in description_data['InformationList']:
            description_info = description_data['InformationList']['Information']
            for info in description_info:
                if 'Description' in info:
                    description = info['Description']
                    break
            else:
                description = 'N/A'
        else:
            description = 'N/A'
        
        # Request compound creation date
        creation_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/dates/JSON"
        creation_response = requests.get(creation_url)
        creation_data = creation_response.json()
        
        if 'InformationList' in creation_data and 'Information' in creation_data['InformationList']:
            creation_info = creation_data['InformationList']['Information']
            for info in creation_info:
                if 'CreationDate' in info:
                    creation_year = info['CreationDate'].get('Year', 'N/A')
                    break
            else:
                creation_year = 'N/A'
        else:
            creation_year = 'N/A'
        
        return compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key, description, creation_year
    
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
    ''' 
compound_info = pubchem_requests(2244)
if compound_info is not None:
    compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key, description, creation_year = compound_info
    print("Compound name:", compound_name)
    print("Chemical formula:", chemical_formula)
    print("Canonical SMILES:", canonical_smiles)
    print("Isomeric SMILES:", isomeric_smiles)
    print("Molecular weight:", molecular_weight)
    print("InChI Key:", inchi_key)
    print("Description:", description)
    print("Creation year:", creation_year)

'''






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


pictogram_urls = get_ghs_pictograms(241)
print(pictogram_urls)











