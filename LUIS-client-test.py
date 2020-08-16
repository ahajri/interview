########### Python 3.6 #############

#
# This quickstart shows how to predict the intent of an utterance by using the LUIS REST APIs.
#

import requests
import json


def test_retrieve_intent_from_luis_engine():
    try:

        ##########
        # Values to modify.

        # YOUR-APP-ID: The App ID GUID found on the www.luis.ai Application Settings page.
        appId = '970927fc-0ec9-4468-a141-219df5d849ad'

        # YOUR-PREDICTION-KEY: Your LUIS authoring key, 32 character value.
        prediction_key = '2c0be813303d4429ac08e9d4d8753cab'

        # YOUR-PREDICTION-ENDPOINT: Replace with your authoring key endpoint.
        # For example, "https://westus.api.cognitive.microsoft.com/"
        prediction_endpoint = 'https://westus.api.cognitive.microsoft.com/'

        # The utterance you want to use.
        utterance = 'I want two large pepperoni pizzas on thin crust please'
        ##########

        # The headers to use in this REST call.
        headers = {
        }

        # The URL parameters to use in this REST call.
        params ={
            'query': utterance,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
            'subscription-key': prediction_key
        }


        # Make the REST call.
        response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict', headers=headers, params=params)

        #validate response http code
        assert response.status_code == 200
        # Display the results on the console.
        print(response.json())
    except Exception as ex:
        assert False, 'Test failed'



