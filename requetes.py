# Récupération de tous les 150 requêtes sous forme de fichier json

import os
from bs4 import BeautifulSoup
import re

dic_requetes = dict() # Dictionnaire dans lequel sera stocké le contenu de tous les requetes

#dict_files = dict()

import os

##### requêtes courtes : avec le champs <title> des topics dans un fichier #####
##### Fonction permettant d'extraire toutes les requetes courtes dans un document de requetes #####
def extraire_requetes_courtes(data):
    # Extraction des numéros
    nums = re.findall(r'<num>(.*?)<dom>', data, re.DOTALL)
    # Néttoyage des extractions et récupération des numéros des requêtes
    num_extrait = ["".join(num.split("Number: ")).strip() for num in nums]
    # Utilisation des expressions régulières pour extraire les champs title des topics
    titles = re.findall(r'<title>(.*?)<desc>', data, re.DOTALL)
    ## Nettoyage des balises titles récupérées pour enlever les espaces superflus et d'en extraire le contenu
    extracted_texts = [" ".join(" ".join(" ".join(title.split("\t")).split("\n")).split("Topic:")).strip() for title in titles]
    #print(num_extrait)
    #print(extracted_texts)
    return dict(zip(num_extrait, extracted_texts))

##### Fonction permettant d'extraire toutes les requetes courtes #####

def extraire_tous_req_courtes(dictio_fichier_req):
    dictio_req = dict()
    for k in dictio_fichier_req.keys():
        dictio_req = {**dictio_req, **extraire_requetes_courtes(dictio_fichier_req[k])}  # Concaténation des dictionnaires

    return dictio_req

# Fonction permettant d'extraire tous les requetes longues d'un fichier de requetes
"""requêtes longues : avec le champs <title> + <desc> des topics
"""
def extraire_requetes_longues(data):
    soup = BeautifulSoup(data, 'html.parser')
    # Extraction des numéros
    nums = re.findall(r'<num>(.*?)<dom>', data, re.DOTALL)
    # Néttoyage des extractions et récupération des numéros
    num_extrait = ["".join(num.split("Number: ")).strip() for num in nums]
    #Utilisation des expressions régulières pour extraire les champs <title> (title) des topics
    titles = re.findall(r'<title>(.*?)<desc>', data, re.DOTALL)
    # Nettoyage des balises titles récupérées pour enlever les espaces superflus et d'en extraire le contenu
    extracted_titles = [" ".join(" ".join(" ".join(title.split("\t")).split("\n")).split("Topic:")).strip() for title in titles]
    # Utilisation des expressions régulières pour extraire les champs <desc> (description) des topics

    # Essayer d'extraire entre <desc> et <smry>
    descrip =  None
    match_smry = re.search(r'<desc>(.*?)<smry>', data, re.DOTALL)
    if match_smry:
        descrip = match_smry.group(1).strip()  # Retourne le texte entre <desc> et <smry>

    # Si <smry> n'existe pas, essayer d'extraire entre <desc> et <narr>
    match_narr = re.search(r'<desc>(.*?)<narr>', data, re.DOTALL)
    if match_narr:
        descrip = match_narr.group(1).strip()


# descs = re.findall(r'<desc>(.*?)<narr>', data, re.DOTALL)
    # Nettoyage des balises titles récupérées pour enlever les espaces superflus et d'en extraire le contenu
    extracted_descs = [" ".join(" ".join(" ".join(descrip.split("\t")).split("\n")).split(":")).strip() for desc in descrip]
    # Formation de la liste des requêtes longues (concatenation des champs title et des champs desc)
    req_longues  = [title + " " + desc for (title, desc) in zip(extracted_titles, extracted_descs)]
    # print(num_extrait)
    # print(extracted_texts)
    return dict(zip(num_extrait, req_longues))







