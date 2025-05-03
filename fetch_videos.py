import requests
import json

API_KEY = 'YOUR_YOUTUBE_API_KEY'  # Remplace par ta clé API YouTube
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

params = {
    'part': 'snippet',
    'maxResults': 5,
    'q': 'comedy',
    'type': 'video',
    'key': API_KEY
}

# Effectuer la requête à l'API YouTube
response = requests.get(BASE_URL, params=params)
data = response.json()

# Récupérer les informations des vidéos
videos = []
for item in data['items']:
    video_info = {
        'title': item['snippet']['title'],
        'url': f"https://www.youtube.com/embed/{item['id']['videoId']}"
    }
    videos.append(video_info)

# Sauvegarder les vidéos dans un fichier JSON
with open('videos.json', 'w') as f:
    json.dump(videos, f)

print("Les vidéos ont été mises à jour avec succès dans 'videos.json'.")
