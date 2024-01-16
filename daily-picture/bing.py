import requests
import json
from cachetools import cached, TTLCache

# Chache will refresh every hour
cache_TTL = 3600

# https://apod.nasa.gov/apod/astropix.html
@cached(cache=TTLCache(maxsize=1, ttl=cache_TTL)) 
def get_bing_url():
    bing_host = "https://www.bing.com"
    api_url = f"{bing_host}/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=nl-nl"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            image_data_object = data["images"][0]
            print(image_data_object)
            return f"{bing_host}{image_data_object["url"]}"

        else:
            return {'error': f'Error {response.status_code} from the NASA picture API'}
    except Exception as e:
        return {'error': f'Error during API call: {str(e)}'}
    