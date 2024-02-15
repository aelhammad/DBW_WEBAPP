import requests
import xml.etree.ElementTree as ET

def get_compound_info(cid):
    # Retrieve compound information from PubChem
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IUPACName,MolecularFormula,CanonicalSMILES,IsomericSMILES,InChIKey,MolecularWeight/JSON"
    response = requests.get(url)
    data = response.json()

    # Check for errors in the response
    if 'Fault' in data:
        print("Error:", data['Fault']['Message'])
        return None
    
    # Extract compound information
    properties = data['PropertyTable']['Properties'][0]
    compound_name = properties.get('IUPACName', 'N/A')
    chemical_formula = properties.get('MolecularFormula', 'N/A')
    canonical_smiles = properties.get('CanonicalSMILES', 'N/A')
    isomeric_smiles = properties.get('IsomericSMILES', 'N/A')
    molecular_weight = properties.get('MolecularWeight', 'N/A')
    inchi_key = properties.get('InChIKey', 'N/A')
    
    return compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key

def get_chembl_id_by_inchikey(inchikey):
    # Search for ChEMBL ID by InChIKey
    url = f"https://www.ebi.ac.uk/chembl/api/data/chembl_id_lookup/search?q={inchikey}"
    response = requests.get(url)

    # Check for errors in the response
    if response.status_code != 200:
        print("Failed to search compound in ChEMBL. Status code:", response.status_code)
        return None

    try:
        # Parse XML response
        root = ET.fromstring(response.content)

        # Extract ChEMBL ID from XML
        chembl_id = root.findtext('.//chembl_id')
        return chembl_id
    except Exception as e:
        print("Failed to parse XML response from ChEMBL:", e)
        return None

# CID of the compound
cid = 2244

# Get compound information from PubChem
compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key = get_compound_info(cid)

if compound_name and chemical_formula:
    print("Name:", compound_name)
    print("Chemical Formula:", chemical_formula)
    print("Canonical SMILES:", canonical_smiles)
    print("Isomeric SMILES:", isomeric_smiles)
    print("Molecular Weight:", molecular_weight)
    print("InChIKey:", inchi_key)

    # Search for compound activities in ChEMBL by InChIKey
    activities = get_chembl_id_by_inchikey(inchi_key)
    if activities:
        print("ChEMBL ID:", activities)
    else:
        print("Failed to retrieve ChEMBL ID from InChIKey.")
else:
    print("Failed to retrieve compound information from PubChem.")
