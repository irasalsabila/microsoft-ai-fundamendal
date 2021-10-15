def get_intent(luis_app_id, cog_key, cog_endpoint, command):
    import json
    import requests

    action = 'unknown'

    try:
        # print the command to be interpreted
        print(command)

        # Set up the REST request
        headers = {
        }
        params ={
            'query': command,
            'subscription-key': cog_key
        }

        # Call the LUIS app and get the prediction
        response = requests.get(cog_endpoint + '/luis/prediction/v3.0/apps/'+ luis_app_id + '/slots/production/predict',
                                headers=headers, params=params)
        data = response.json()

        # Get the most probable intent
        intent = data["prediction"]["topIntent"]
        print('- predicted intent:',intent)

        if intent != 'None':
            # Get the target pizza
            entities = data["prediction"]["entities"]
            if 'pizza' in entities:
                # For simplicity, only the first 'pizza' entity is identified
                pizza = entities['pizza']#[:][0]
                
                print('- predicted entity:',pizza + pizza + pizza)

                # Set the action to intent_pizza
                action = intent + '_' +  pizza

        return action

    except Exception as ex:
        print(ex)
        return 'unknown'
