import json
import os
import gzip
import shutil
from requetes import extraire_requetes_longues, extraire_requetes_courtes

import os
import gzip
import shutil

import os
import gzip
import shutil

# Chemins des dossiers
input_folder = '/home/alimijileking/PycharmProjects/Solr_project/AP'
output_folder = '/home/alimijileking/PycharmProjects/Solr_project/AP_ok'

# Vérifie que le dossier de sortie existe, sinon le crée
os.makedirs(output_folder, exist_ok=True)

import os

import os
import chardet

# Chemins des dossiers
input_folder = '/home/alimijileking/PycharmProjects/Solr_project/AP__ok'
output_folder = '/home/alimijileking/PycharmProjects/Solr_project/AP_fixed'

# Crée le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)


# Fonction pour détecter l'encodage
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']


# Fonction pour transformer un document en structure XML Solr
def transform_document(lines):
    doc_lines = []
    doc_lines.append("  <doc>")  # Début du document
    for line in lines:
        line = line.strip()
        if line.startswith("<DOCNO>"):
            content = line.replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
            doc_lines.append(f"    <field name=\"DOCNO\">{content}</field>")
        elif line.startswith("<FILEID>"):
            content = line.replace("<FILEID>", "").replace("</FILEID>", "").strip()
            doc_lines.append(f"    <field name=\"FILEID\">{content}</field>")
        elif line.startswith("<FIRST>"):
            content = line.replace("<FIRST>", "").replace("</FIRST>", "").strip()
            doc_lines.append(f"    <field name=\"FIRST\">{content}</field>")
        elif line.startswith("<SECOND>"):
            content = line.replace("<SECOND>", "").replace("</SECOND>", "").strip()
            doc_lines.append(f"    <field name=\"SECOND\">{content}</field>")
        elif line.startswith("<HEAD>"):
            content = line.replace("<HEAD>", "").replace("</HEAD>", "").strip()
            doc_lines.append(f"    <field name=\"HEAD\">{content}</field>")
        elif line.startswith("<DATELINE>"):
            content = line.replace("<DATELINE>", "").replace("</DATELINE>", "").strip()
            doc_lines.append(f"    <field name=\"DATELINE\">{content}</field>")
        elif line.startswith("<TEXT>"):
            content = line.replace("<TEXT>", "").replace("</TEXT>", "").strip()
            doc_lines.append(f"    <field name=\"TEXT\">{content}</field>")
    doc_lines.append("  </doc>")  # Fin du document
    return doc_lines


# Parcourt tous les fichiers XML dans le dossier d'entrée
for filename in os.listdir(input_folder):
    if filename.endswith('.xml'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Détecte l'encodage
            encoding = detect_encoding(input_path)
            print(f"Encodage détecté pour {filename}: {encoding}")

            # Lit le fichier avec l'encodage détecté
            with open(input_path, 'r', encoding=encoding, errors='ignore') as file:
                lines = file.readlines()

            # Transforme et écrit dans le fichier de sortie
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write("<add>\n")  # Début de la racine Solr
                current_doc = []
                in_doc = False
                for line in lines:
                    if "<DOC>" in line:  # Début d'un document
                        in_doc = True
                        current_doc = []
                    elif "</DOC>" in line:  # Fin d'un document
                        in_doc = False
                        # Transforme le document et l'écrit dans le fichier
                        transformed_doc = transform_document(current_doc)
                        out_file.write("\n".join(transformed_doc) + "\n")
                    elif in_doc:
                        current_doc.append(line)
                out_file.write("</add>\n")  # Fin de la racine Solr

            print(f"Fichier corrigé et converti : {output_path}")

        except Exception as e:
            print(f"Erreur lors du traitement de {filename}: {e}")

"""
# Parcourt tous les fichiers du dossier d'entrée
for filename in os.listdir(input_folder):
    if filename.endswith('.gz'):  # Vérifie si le fichier est au format .gz
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename[:-3] + '.xml')  # Supprime '.gz' et ajoute '.xml'

        # Décompresse le fichier et l'écrit directement avec l'extension .xml
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f"Fichier extrait et enregistré en XML : {output_path}")"""

"""




# Creation des requetes longues

# Liste des fichiers à traiter
files = ['Topics-requetes/topics.1-50.txt', 'Topics-requetes/topics.51-100.txt', 'Topics-requetes/topics.101-150.txt']

# Dictionnaire pour stocker les résultats
def lire_fichier(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
req_longues_combines = {}

req_courtes_combines = {}

for fichier in files:
    data = lire_fichier(fichier)
    resultat = extraire_requetes_longues(data)
    req_longues_combines.update(resultat)

for fichier in files:
    data = lire_fichier(fichier)
    resultat = extraire_requetes_courtes(data)
    req_courtes_combines.update(resultat)
"""
# Afficher les résultats combinés
#print(resultats_combines)

# Convertion en fichier json

# Conversion en fichier JSON
"""
with open('requetes/requetes_longues.json', 'w', encoding='utf-8') as fichier_json:
    json.dump( req_longues_combines, fichier_json, ensure_ascii=False, indent=4)


# Creation des requetes courtes

with open('requetes/requetes_courtes.json', 'w', encoding='utf-8') as fichier_json:
    json.dump( req_courtes_combines, fichier_json, ensure_ascii=False, indent=4)

"""


