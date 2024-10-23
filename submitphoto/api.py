from __future__ import print_function
import time
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from pprint import pprint

import submitphoto.config as config

def configure_api():
    # Configure API key authorization: Apikey
    configuration = cloudmersive_ocr_api_client.Configuration()
    configuration.api_key['Apikey'] = config.api_key

    # create an instance of the API class
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))

    return api_instance


def get_text(path):
    api_instance = configure_api()
    try:
        # Convert a photo of a document into text
        api_response = api_instance.image_ocr_photo_to_text(path)
        return api_response
    except ApiException as e:
        print("Exception when calling ImageOcrApi->image_ocr_photo_to_text: %s\n" % e)



