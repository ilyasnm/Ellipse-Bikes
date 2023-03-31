import json
import requests

# Clé API
api_key = "e0a1bf2c844edb9084efc764c089dd748676cc14"

# URL de l'API
url = "https://api.jcdecaux.com/vls/v3/"

# Liste des villes à analyser
villes = ["nantes", "lyon", "dublin", "toulouse", "santander"]

# Récupération des données pour chaque ville
for ville in villes:
    # URL pour la ville donnée
    ville_url = url + "stations?contract=" + ville + "&apiKey=" + api_key
    # Récupération des données
    response = requests.get(ville_url)
    data = response.json()
   # print(data)
  
    
    # Calcul du nombre de vélos total et le nombre de vélos électriques
    nb_velos_electriques = sum([x['totalStands']['availabilities'].get('electricalBikes', 0) if 'totalStands' in x else 0 for x in data])
    nb_velos_mecaniques = sum([x['totalStands']['availabilities'].get('mechanicalBikes', 0) if 'totalStands' in x else 0 for x in data])
    nb_velos_total = nb_velos_electriques + nb_velos_mecaniques
    
    print(f"Pour la ville de {ville} :")
    print(f"Nombre de vélos total : {nb_velos_total}")
    print(f"Nombre de vélos électriques : {nb_velos_electriques}")
    print(f"Nombre de vélos mécaniques : {nb_velos_mecaniques}")
    print()
    
    # Calcul du pourcentage de vélos électriques et mécaniques
    if nb_velos_total==0:
          pourcentage_velos_electriques=0
          pourcentage_velos_mecaniques=0
          
    else:      
        pourcentage_velos_electriques = (nb_velos_electriques / nb_velos_total) * 100
        pourcentage_velos_mecaniques = (nb_velos_mecaniques / nb_velos_total) * 100
    # Affichage des résultats pour chaque ville
    print("Ville:", ville.capitalize())
    print("Nombre de vélos total:", nb_velos_total)
    print("Pourcentage de vélos électriques:", round(pourcentage_velos_electriques, 2), "%")
    print("Pourcentage de vélos mécaniques:", round(pourcentage_velos_mecaniques, 2), "%")
    print("-------------------------------")
    
# Classement des villes avec le plus grand nombre de vélos
villes_classement = {}
for ville in villes:
    ville_url = url + "stations?contract=" + ville + "&apiKey=" + api_key
    response = requests.get(ville_url)
    data = response.json()
    nb_velos_total = len(data)
    villes_classement[ville] = nb_velos_total
villes_classement = dict(sorted(villes_classement.items(), key=lambda x: x[1], reverse=True))
print("Classement des villes avec le plus grand nombre de vélos:")
for ville, nb_velos in villes_classement.items():
    print(ville.capitalize(), ":", nb_velos)


