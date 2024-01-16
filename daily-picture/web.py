import os
from flask import Flask, send_file
from io import BytesIO

from nasa import get_APOD_url, get_EPIC_url
from bing import get_bing_url
from helper import retrieve_image_from_url


NASA_api_key_variable = 'NASA_API_KEY'

app = Flask(__name__)

def return_picture(image_data):
    if image_data:
        # Serve the image using Flask
        return send_file(BytesIO(image_data), mimetype='image/jpeg')
    else:
        return 'Image retrieval failed'


@app.route('/NASA/epic')
def get_NASA_epic_image():
    #This one is a bit slow, the EPIC API takes a while to respond
    image = retrieve_image_from_url(get_EPIC_url(os.environ.get(NASA_api_key_variable, "DEMO_KEY")))
    return return_picture(image)

@app.route('/NASA/apod')
def get_NASA_apod_image():
    image = retrieve_image_from_url(get_APOD_url(os.environ.get(NASA_api_key_variable, "DEMO_KEY")))
    return return_picture(image)

@app.route('/bing')
def get_bing_image():
    image = retrieve_image_from_url(get_bing_url())
    return return_picture(image)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()