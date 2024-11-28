import pysolr
import json

from requete_resultat_solr import resultats_requetes


# Configuration de base
solr_url = "http://localhost:8983/solr"

schemas = ["Bm25", "Tfidf"]  # Remplacez par vos champs configurés
collections = ["Bm25_standard", "Tfidf_standard", "Bm25_pret", "Tfidf_pret"]
requetes = []  # Liste des requêtes: requêtes de test


# resultats_requetes(solr_url, collection_name, schema, requetes_file,  chemin_fichier )

### Tfidf standard (sans pretraitement)

collection_name = collections[1]
schema = schemas[1]
small_requetes_file = "requetes/requetes_courtes.json"
long_requetes_file = "requetes/requetes_longues.json"

resultat_small_req_tfidf = "resultats_requetes/resultat_small_req_tfidf_base.txt"
resultat_long_req_tfidf = "resultats_requetes/resultat_long_req_tfidf_base.txt"

resultats_requetes(solr_url, collection_name, schema, small_requetes_file, resultat_small_req_tfidf)

resultats_requetes(solr_url, collection_name, schema, long_requetes_file,  resultat_long_req_tfidf)

### Tfidf avec pretaitement

collection_name = collections[3]
schema = schemas[1]
small_requetes_file = "requetes/requetes_courtes.json"
long_requetes_file = "requetes/requetes_longues.json"

resultat_small_req_tfidf = "resultats_requetes/resultat_small_req_tfidf_pret.txt"
resultat_long_req_tfidf = "resultats_requetes/resultat_long_req_tfidf_pret.txt"

resultats_requetes(solr_url, collection_name, schema, small_requetes_file, resultat_small_req_tfidf)

resultats_requetes(solr_url, collection_name, schema, long_requetes_file,  resultat_long_req_tfidf)