import requests


def retrieve_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return response.content
        else:
            return None  # Return None to indicate an error
    except Exception as e:
        print(f'Error during image retrieval: {str(e)}')
        return None
