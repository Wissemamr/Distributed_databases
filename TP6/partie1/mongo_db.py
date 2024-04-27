import pymongo
client = pymongo.MongoClient("localhost", 27017) 
print('[CONNEXION ETABLIE]')

db = client["TP6_DB"]
print('[ACCES REUSSI A LA BDD]')

collection = db["collection_tp6_2"]
print('[ACCES REUSSI A LA COLLECTION]')



# data = {"name": "WIZZAL", "age": 22, "city": "Berlin", "car": "BMW-M5-CS"}
# collection.insert_one(data)
# print('[INSERTION REUSSIE]')



data = {"name": "MUXDEMUX", "age": 15, "city": "Toronto", "car": "Chevrolet-camaro"}
collection.insert_one(data)
print('[INSERTION REUSSIE]')


# recherche par nom
query = {"name": "WIZZAL"}
resultat = collection.find_one(query)
print(f'[RESULTAT : {resultat}]')

# mise à jour
new_value = {"$set": {"age": 23}}
collection.update_one(query, new_value)
print('[MAJ REUSSIE]')


# suppression
query_ = {"age": 15}
collection.delete_one(query_)
print('[SUPPRESSION REUSSIE]')