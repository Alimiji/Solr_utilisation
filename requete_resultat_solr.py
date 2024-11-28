import pysolr
import os
import json
import requests




##### Cette fonction permet de récupèrer les 1000 premiers documents pour chaque requête

import requests

def executer_requete_pour_trec_eval(solr_url, collection_name, schema, requete, query_id, type_requete:str):

    #schema = "text_tfidf_no_preprocessing"
    #requete = 'Design of the "Star Wars" Anti-missile Defense System'
    # type_requete = req_courte ou req_longue
    params = {
        "q": requete,
         "qf": "TEXT^2.0 HEAD^1.0", # Pondération de recherche dans chaque champ
        "fl": "DOCNO, score",
        "rows": 1000,
    }

    response = requests.get(f"{solr_url}/{collection_name}/select", params=params)
    data = response.json()

    # Formatter les résultats pour trec_eval
    results_for_trec_eval = []
    for rank, doc in enumerate(data['response']['docs']):
        line = f"{query_id} Q0 {doc['id_doc'][0]} {rank} {doc['score']} {collection_name + "_" + type_requete}"
        results_for_trec_eval.append(line)

    print("\n")
    print("Format de trec_eval: ", results_for_trec_eval)


    return results_for_trec_eval






##### Cette fonction permet de récupérer les résultats(1000 documents) pour chaque requête
##### et stocke tous dans un fichier

def resultats_requetes(solr_url, collection_name, schema, requetes_file,  chemin_fichier ): # requetes étant un dictionnaire de requêtes


    requetes = dict()
    # Lecture et conversion en dictionnaire
    with open(requetes_file, "r", encoding="utf-8") as json_file:
        requetes = json.load(json_file)

    results_for_trec_eval = []
    for query_id, requete in requetes.items():
        reponse = executer_requete_pour_trec_eval(solr_url, collection_name, schema, requete, query_id)
        results_for_trec_eval = results_for_trec_eval + reponse

    # Ouvrir le fichier en mode écriture
    with open(chemin_fichier, "w") as fichier:
        for chaine in results_for_trec_eval:
            # Écrire chaque chaîne de caractères dans le fichier
            fichier.write(chaine + "\n")  # Ajouter un saut de ligne après chaque chaîne

    print(f"Fichier '{chemin_fichier}' créé avec succès.")

