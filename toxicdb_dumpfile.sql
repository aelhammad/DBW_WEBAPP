-- MySQL dump 10.13  Distrib 8.3.0, for macos14.2 (arm64)
--
-- Host: localhost    Database: toxbrowser
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `entry`
--

DROP TABLE IF EXISTS `entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entry` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pubchem_id` varchar(20) NOT NULL,
  `chembl_id` varchar(20) NOT NULL,
  `inchi_key` varchar(30) NOT NULL,
  `chemical_formula` varchar(50) NOT NULL,
  `compound_name` varchar(200) NOT NULL,
  `molecular_weight` float DEFAULT NULL,
  `description` text,
  `description1` text,
  `canonical_smiles` varchar(200) DEFAULT NULL,
  `isomeric_smiles` varchar(200) DEFAULT NULL,
  `mechanism_of_toxicity` text,
  `treatment` text,
  `year_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `year_id` (`year_id`),
  CONSTRAINT `entry_ibfk_1` FOREIGN KEY (`year_id`) REFERENCES `year` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entry`
--

LOCK TABLES `entry` WRITE;
/*!40000 ALTER TABLE `entry` DISABLE KEYS */;
INSERT INTO `entry` VALUES (1,'241','CHEMBL277500','UHOVQNZJYSORNB-UHFFFAOYSA-N','C6H6','benzene',78.11,'Benzene is a six-carbon aromatic annulene in which each carbon atom donates one of its two 2p electrons into a delocalised pi system. A toxic, flammable liquid byproduct of coal distillation, it is used as an industrial solvent. Benzene is a carcinogen that also damages bone marrow and the central nervous system. It has a role as a non-polar solvent, a carcinogenic agent and an environmental contaminant. It is an aromatic annulene, a volatile organic compound and a member of benzenes.','Benzene is a toxic, volatile, flammable liquid hydrocarbon biproduct of coal distillation. Chronic benzene exposure produces hematotoxicity, bone marrow dysplasia (Displasia is a pre-neoplastic or pre-cancerous change). (A7669). It is used as an industrial solvent in paints, varnishes, lacquer thinners, gasoline, etc. Benzene causes central nervous system damage acutely and is carcinogenic. It was formerly used as parasiticide.','C1=CC=CC=C1','C1=CC=CC=C1','The toxic agents of benzene are its metabolites. Benzene is able increase its toxicity by inducing cytochrome P450 2E1, its main metabolic enzyme. Benzene\'s primary toxic effects are decreases in haematological cell counts and bone marrow cellularity. The decrease in blood cell count may be due to the binding of metabolites such as benzene oxide to the blood proteins albumin and haemoglobin. In the bone marrow, phenolic metabolites can be metabolized by bone marrow peroxidases to highly reactive semiquinone radicals and quinones that stimulate the production of reactive oxygen species. This and direct metabolite binding leads to damage to tubulin, histone proteins, and topoisomerase II. Some metabolites also exert mutagenic effects by inhibiting other DNA associated proteins, such as mitochondrial DNA polymerase and ribonucleotide reductase, as well as covalently binding to DNA itself, causing effects such as strand breakage, mitotic recombination, chromosome translocations, and aneuploidy. (L5)','There is no known antidote for benzene and poisoning is first treated by preventing further exposure. If inhaled, respiratory assist may be necessary. If ingested, gastric lavage may be performed, or activated charcoal can be administered. (T8)',1),(2,'6212','CHEMBL44618','HEDRZPFGACZZDS-UHFFFAOYSA-N','CHCl3','chloroform',119.37,'Chloroform is a one-carbon compound that is methane in which three of the hydrogens are replaced by chlorines. It has a role as an inhalation anaesthetic, a non-polar solvent, a carcinogenic agent, a central nervous system drug and a refrigerant. It is a one-carbon compound and a member of chloromethanes.','Chloroform is found in spearmint. Indirect food additive arising from adhesives and polymers Chloroform is a common solvent in the laboratory because it is relatively unreactive, miscible with most organic liquids, and conveniently volatile. Chloroform is used as a solvent in the pharmaceutical industry and for producing dyes and pesticides. Chloroform is an effective solvent for alkaloids in their base form and thus plant material is commonly extracted with chloroform for pharmaceutical processing. For example, it is commercially used to extract morphine from poppies and scopolamine from Datura plants. Chloroform containing deuterium (heavy hydrogen), CDCl3, is a common solvent used in NMR spectroscopy. It can be used to bond pieces of acrylic glass (also known under the trade names Perspex and Plexiglas). Chloroform is a solvent of phenol:chloroform:isoamyl alcohol 25:24:1 is used to dissolve non-nucleic acid biomolecules in DNA and RNA extractions. Chloroform is the organic compound with formula CHCl3. It does not undergo combustion in air, although it will burn when mixed with more flammable substances. It is a member of a group of compounds known as trihalomethanes. Chloroform has myriad uses as a reagent and a solvent. It is also considered an environmental hazard. Several million tons are produced annually. The output of this process is a mixture of the four chloromethanes: chloromethane, dichloromethane, chloroform (trichloromethane), and carbon tetrachloride, which are then separated by distillation.\r\rChloroform has been shown to exhibit antifoaming agent, anti-coagulant, depressant, analgesic and anti-fungal functions (A7671, A7672, A7673, A7674, A7675).\r\rChloroform belongs to the family of Organochlorides. These are organic compounds containing a chlorine atom.','C(Cl)(Cl)Cl','C(Cl)(Cl)Cl','Chloroform and the reactive intermediates of chloroform metabolism, especially phosgene, bind covalently and irreversibly to cellular macromolecules and cause cellular damage within the liver and kidney. While the exact mechanism is unknown, phosgene has been shown to react with molecules such as cysteine, deplete hepatic glutathione, form adducts with microsomal proteins, and elevate hepatic enzyme levels. Chloroform has also been shown to block HERG potassium channels, causing cardiac arrest. (L13, A11, A29)','There is no known antidote for chloroform. Exposure is usually handled with symptomatic treatment. (L13)',1),(3,'969491','CHEMBL1873703','DFBKLUNHFCTMDC-PICURKEMSA-N','C12H8Cl6O','(1R,2S,3S,6R,7R,8S,9S,11R)-3,4,5,6,13,13-hexachloro-10-oxapentacyclo[6.3.1.13,6.02,7.09,11]tridec-4-ene',380.9,'Dieldrin is an organochlorine compound resulting from the epoxidation of the double bond of aldrin. It is the active metabolite of the proinsecticde aldrin. It has a role as a xenobiotic and a carcinogenic agent. It is an organochlorine insecticide, an organochlorine compound and an epoxide. It is functionally related to an aldrin.','Dieldrin is a chlorinated hydrocarbon used as an insecticide, either by itself or as a component of the closely related insectide aldrin. As dieldrin is neurotoxin and tends to bioaccumulate, its use is now banned in most parts of the world. (L86) Dieldrin is a chlorinated hydrocarbon originally produced in 1948 by J. Hyman & Co, Denver, as an insecticide. Dieldrin is closely related to aldrin, which reacts further to form dieldrin. Aldrin is not toxic to insects; it is oxidized in the insect to form dieldrin which is the active compound. Both dieldrin and aldrin are named after the Diels-Alder reaction which is used to form aldrin from a mixture of norbornadiene and hexachlorocyclopentadiene.','C1C2C3C(C1C4C2O4)C5(C(=C(C3(C5(Cl)Cl)Cl)Cl)Cl)Cl','C1[C@@H]2[C@H]3[C@@H]([C@H]1[C@H]4[C@@H]2O4)[C@]5(C(=C([C@@]3(C5(Cl)Cl)Cl)Cl)Cl)Cl','Dieldrin antagonizes the action of the neurotransmitter gamma-aminobutyric acid (GABA) acting at the GABA-A receptors, effectively blocking the GABA-induced uptake of chloride ions. Dieldrin also inhibits Na+ K+ ATPase and Ca2+ and Mg2+ ATPase which are essential for the transport of calcium across membranes. This results in the accumulation of intracellular free calcium ions, which promotes release of neurotransmitters from storage vesicles, the subsequent depolarization of adjacent neurons, and the propagation of stimuli throughout the CNS. This results in hyperexcitation and generalized seizures. Dieldrin also binds to alpha-synuclein, leading to the formation of intracellular fibrils. (T10, L87)','Treatment is symptomatic, aimed at controlling convulsions, coma, and respiratory depression. If ingested, gastric lavage may be performed, followed by administering activated charcoal powder. (L143)',2),(4,'7111','CHEMBL15901','HFACYLZERDEVSX-UHFFFAOYSA-N','C12H12N2','4-(4-aminophenyl)aniline',184.24,'Benzidine is a member of the class of biphenyls that is 1,1\'-biphenyl in which the hydrogen at the para-position of each phenyl group has been replaced by an amino group. It has a role as a carcinogenic agent. It is a member of biphenyls and a substituted aniline.','Benzidine is the organic compound with the formula (C6H4NH2)2. it is an aromatic amine. It is prepared in a two step process from nitrobenzene. First, the nitrobenzene is converted to 1,2-diphenylhydrazine, usually using iron powder as the reducing agent. Treatment of this hydrazine with mineral acids induces a rearrangement reaction to 4,4\'-benzidine. Smaller amounts of other isomers are also formed. The benzidine rearrangement, which proceeds intramolecularly, is a classic mechanistic puzzle in organic chemistry.  This aromatic amine is a component of a test for cyanide and also in the production of dyes. Benzidine has been linked to bladder and pancreatic cancer. Since August 2010 benzidine dyes are included in the EPA\'s List of Chemicals of Concern.','C1=CC(=CC=C1C2=CC=C(C=C2)N)N','C1=CC(=CC=C1C2=CC=C(C=C2)N)N','N-acetylated benzidine metabolites are believed to form adducts with nucleic acids. Carcinogenesis is initiated when they are activated by peroxidation by prostaglandin H synthetase, oxidation by cytochrome P-450, or O-esterification by O-acetyltransferase or N,O-acetyltransferase. Benzidine has also been shown to bind to RNA and hemoglobin. (L95, A55)','',2),(5,'3589','CHEMBL194400','FRCCEHPWNOQAEU-UHFFFAOYSA-N','C10H5Cl7','1,5,7,8,9,10,10-heptachlorotricyclo[5.2.1.02,6]deca-3,8-diene',373.3,'Heptachlor is a cyclodiene organochlorine insecticide that is 3a,4,7,7a-tetrahydro-1H-4,7-methanoindene substituted by chlorine atoms at positions 1, 4, 5, 6, 7, 8 and 8. Formerly used to kill termites, ants and other insects in agricultural and domestic situations. It has a role as a GABA-gated chloride channel antagonist, an agrochemical, an antibacterial agent, a persistent organic pollutant and an antifungal agent. It derives from a hydride of a 1H-indene.','Heptachlor is a manufactured cyclodiene organochlorine insecticide. As it is a persistant organic pollutant, heptachlor use is banned or limited in most areas. It is one ingredient of cigarette. (L118, L119)','C1=CC(C2C1C3(C(=C(C2(C3(Cl)Cl)Cl)Cl)Cl)Cl)Cl','C1=CC(C2C1C3(C(=C(C2(C3(Cl)Cl)Cl)Cl)Cl)Cl)Cl','Heptachlor is a central nervous system stimulant. It non-competitively blocks neurotransmitter action at gamma-amino butyric acid receptors, resulting in overstimulation of the nervous system. Heptachlor is also believed to exert carcinogenic effects by activating key kinases in signalling pathways and inhibiting apoptosis. (L118, A81, A82)','Treatment is symptomatic and is aimed at controlling convulsions, coma, and respiratory depression. (L118)\r\n',2);
/*!40000 ALTER TABLE `entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entry_pictogram_association`
--

DROP TABLE IF EXISTS `entry_pictogram_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entry_pictogram_association` (
  `entry_id` int DEFAULT NULL,
  `pictogram_id` int DEFAULT NULL,
  KEY `entry_id` (`entry_id`),
  KEY `pictogram_id` (`pictogram_id`),
  CONSTRAINT `entry_pictogram_association_ibfk_1` FOREIGN KEY (`entry_id`) REFERENCES `entry` (`id`),
  CONSTRAINT `entry_pictogram_association_ibfk_2` FOREIGN KEY (`pictogram_id`) REFERENCES `pictograms` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entry_pictogram_association`
--

LOCK TABLES `entry_pictogram_association` WRITE;
/*!40000 ALTER TABLE `entry_pictogram_association` DISABLE KEYS */;
INSERT INTO `entry_pictogram_association` VALUES (1,1),(1,2),(2,3),(2,2),(2,4),(2,5),(3,4),(4,3),(5,2),(5,4);
/*!40000 ALTER TABLE `entry_pictogram_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entry_type_names_association`
--

DROP TABLE IF EXISTS `entry_type_names_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entry_type_names_association` (
  `entry_id` int DEFAULT NULL,
  `type_name_id` int DEFAULT NULL,
  KEY `entry_id` (`entry_id`),
  KEY `type_name_id` (`type_name_id`),
  CONSTRAINT `entry_type_names_association_ibfk_1` FOREIGN KEY (`entry_id`) REFERENCES `entry` (`id`),
  CONSTRAINT `entry_type_names_association_ibfk_2` FOREIGN KEY (`type_name_id`) REFERENCES `type_name` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entry_type_names_association`
--

LOCK TABLES `entry_type_names_association` WRITE;
/*!40000 ALTER TABLE `entry_type_names_association` DISABLE KEYS */;
INSERT INTO `entry_type_names_association` VALUES (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(2,1),(2,14),(2,4),(2,15),(2,6),(2,7),(2,16),(2,8),(2,9),(2,10),(2,11),(2,12),(2,17),(3,1),(3,14),(3,6),(3,18),(3,7),(3,17),(4,1),(4,3),(4,19),(4,7),(4,9),(4,12),(4,17),(5,1),(5,14),(5,6),(5,7),(5,10),(5,17);
/*!40000 ALTER TABLE `entry_type_names_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_effects`
--

DROP TABLE IF EXISTS `health_effects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `health_effects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `entry_id` int NOT NULL,
  `health_effects` text,
  PRIMARY KEY (`id`),
  KEY `entry_id` (`entry_id`),
  CONSTRAINT `health_effects_ibfk_1` FOREIGN KEY (`entry_id`) REFERENCES `entry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_effects`
--

LOCK TABLES `health_effects` WRITE;
/*!40000 ALTER TABLE `health_effects` DISABLE KEYS */;
INSERT INTO `health_effects` VALUES (1,1,'Benzene causes harmful effects on the bone marrow and also decreases blood cell counts, leading to blood disorders such as anemia. It can also cause excessive bleeding and affect the immune system, increasing the chance for infection. Benzene is also a known carcinogen, as chronic exposure to high levels has been shown to cause leukemia, particularly acute myelogenous leukemia. (L5)'),(2,2,'Chronic exposure to chloroform causes liver and kidney damage. It has also been shown to have detrimental reproductive and developmental effects. Skin contact with large amounts of chloroform results in sores. Inhaling large amounts of chloroform can cause central nervous system and respiratory depression, and may be fatal. (L13)'),(3,3,'Dieldrin is a neurotoxin and works by overstimulating the central nervous system. Ingestion of large amounts of dieldrin causes convulsions and death. However, chronic exposure to lower amounts of dieldrin also has adverse effects because dieldrin accumulates in the body. Dieldrin is known to damage the nervous system, liver, and immune system. (L87)'),(4,4,'Benzidine is a known human carcinogen, most often associated with cancer of the urinary bladder. If benzidine comes in contact with skin it may cause a skin allergy. Liver, kidney, immune, and neurological effects have also been observed in animals exposed to benzidine. (L95)'),(5,5,'Exposure to heptachlor may cause damage to your liver, nervous system, and immune system. (L118)');
/*!40000 ALTER TABLE `health_effects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pictograms`
--

DROP TABLE IF EXISTS `pictograms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pictograms` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pictogram_url` text NOT NULL,
  `entry_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `entry_id` (`entry_id`),
  CONSTRAINT `pictograms_ibfk_1` FOREIGN KEY (`entry_id`) REFERENCES `entry` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pictograms`
--

LOCK TABLES `pictograms` WRITE;
/*!40000 ALTER TABLE `pictograms` DISABLE KEYS */;
INSERT INTO `pictograms` VALUES (1,'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS02.svg',NULL),(2,'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS09.svg',NULL),(3,'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS07.svg',NULL),(4,'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS06.svg',NULL),(5,'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS05.svg',NULL);
/*!40000 ALTER TABLE `pictograms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_name`
--

DROP TABLE IF EXISTS `type_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_name` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_name` (`type_name`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_name`
--

LOCK TABLES `type_name` WRITE;
/*!40000 ALTER TABLE `type_name` DISABLE KEYS */;
INSERT INTO `type_name` VALUES (19,'Amine'),(3,'Aromatic Hydrocarbon'),(10,'Cigarette Toxin'),(16,'Drug'),(18,'Ether'),(8,'Food Toxin'),(5,'Gasoline Additive/Component'),(11,'Household Toxin'),(15,'Indicator and Reagent'),(2,'Industrial Precursor/Intermediate'),(12,'Industrial/Workplace Toxin'),(9,'Metabolite'),(13,'Natural Compound'),(1,'Organic Compound'),(14,'Organochloride'),(6,'Pesticide'),(7,'Pollutant'),(4,'Solvent'),(17,'Synthetic Compound');
/*!40000 ALTER TABLE `type_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(40) NOT NULL,
  `password` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_entries`
--

DROP TABLE IF EXISTS `user_entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_entries` (
  `entry_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  KEY `entry_id` (`entry_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_entries_ibfk_1` FOREIGN KEY (`entry_id`) REFERENCES `entry` (`id`),
  CONSTRAINT `user_entries_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_entries`
--

LOCK TABLES `user_entries` WRITE;
/*!40000 ALTER TABLE `user_entries` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_entries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userdata` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `surname` varchar(40) NOT NULL,
  `institution` varchar(40) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `userdata_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `year`
--

DROP TABLE IF EXISTS `year`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `year` (
  `id` int NOT NULL AUTO_INCREMENT,
  `creation_year` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `year`
--

LOCK TABLES `year` WRITE;
/*!40000 ALTER TABLE `year` DISABLE KEYS */;
INSERT INTO `year` VALUES (1,2004),(2,2005);
/*!40000 ALTER TABLE `year` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-04 20:09:09
