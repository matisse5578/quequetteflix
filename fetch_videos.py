import requests
from bs4 import BeautifulSoup
import json

# Fonction pour récupérer les vidéos YouTube intégrées via <iframe> sur un site
def get_youtube_video_links(url):
    # Faire une requête GET pour obtenir la page
    response = requests.get(url)
    
    # Si la requête a réussi (code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Liste pour stocker les liens vidéo YouTube
        video_links = []
        
        # Rechercher les balises <iframe> avec des liens YouTube
        for iframe in soup.find_all('iframe'):
            src = iframe.get('src')
            if src and 'youtube.com/embed/' in src:
                video_links.append(src)  # Ajouter le lien vidéo à la liste

        return video_links
    else:
        print(f"Erreur: Impossible de récupérer la page {url}")
        return []

# Fonction pour ajouter des vidéos dans le fichier video.json existant
def add_videos_to_json(videos, video_json_file="video.json"):
    try:
        # Charger les données existantes du fichier JSON
        with open(video_json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        # Si le fichier n'existe pas, créer une structure de base
        data = {"nouveauter": []}  # Utiliser "nouveauter" comme clé
    
    # Ajouter les nouvelles vidéos à la liste sous la clé "nouveauter"
    for video in videos:
        data["nouveauter"].append({"url": video})
    
    # Sauvegarder les données mises à jour dans le fichier JSON
    with open(video_json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Les vidéos ont été ajoutées sous la clé 'nouveauter' dans {video_json_file}")

# Exemple d'utilisation
url = "https://exemple.com"  # Remplace cette URL par l'URL du site contenant des vidéos YouTube intégrées

# Récupérer les liens vidéo depuis le site
videos = get_youtube_video_links(url)

if videos:
    print("Vidéos YouTube trouvées :", videos)
    # Ajouter les vidéos récupérées à video.json sous la clé "nouveauter"
    add_videos_to_json(videos)
else:
    print("Aucune vidéo YouTube trouvée sur la page.")
