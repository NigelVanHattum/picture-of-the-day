import requests
import json
from datetime import datetime
from cachetools import cached, TTLCache

# Chache will refresh every hour
cache_TTL = 3600

# https://apod.nasa.gov/apod/astropix.html
@cached(cache=TTLCache(maxsize=1, ttl=cache_TTL)) 
def get_APOD_url(api_key):
    api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            return data["url"]
        else:
            return {'error': f'Error {response.status_code} from the NASA picture API'}
    except Exception as e:
        return {'error': f'Error during API call: {str(e)}'}
    
# https://epic.gsfc.nasa.gov/
@cached(cache=TTLCache(maxsize=1, ttl=cache_TTL))
def get_EPIC_url(api_key):
    api_url = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}"
    print("Doing something")

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            picture_date = datetime.strptime(data[0]["date"], "%Y-%m-%d %H:%M:%S")
            picture_id = data[0]["image"]
            image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{picture_date.year}/{'{:02d}'.format(picture_date.month)}/{'{:02d}'.format(picture_date.day)}/png/{picture_id}.png"
            print(image_url)
            return image_url
        else:
            return {'error': f'Error {response.status_code} from the NASA picture API'}
    except Exception as e:
        return {'error': f'Error during API call: {str(e)}'}