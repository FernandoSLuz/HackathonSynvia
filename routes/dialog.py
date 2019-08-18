import json
import os

import flask
from flask import request


blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/dialog', methods=[ 'GET', 'POST' ])
def dialog():
    
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    print("Request:" + res)
    if(res is 'null'):
        return {'fulfillmentText': 'response error'}
    else:
        responseText = ''
        intentName = form['queryResult']['intent']['displayName']
        if(intentName == 'Teste') :
            responseText = form['queryResult']['queryText']
            return {'fulfillmentText': "Texto digitado: " + responseText}
        else:
            return {'fulfillmentText': "Intent " + intentName + " not listed on our database"}
