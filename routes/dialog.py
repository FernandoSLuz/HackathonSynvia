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
        required_attributes = [ 'displayName', 'queryText']
        for attr in required_attributes:
            if attr not in form:
                return flask.jsonify({
                    'fulfillmentText': 'attribute {} required'.format(attr)
                }), 400
        displayName, queryText = [form[key] for key in required_attributes ]        
        response = displayName + ' ----  queryText: ' + queryText 
        return {'fulfillmentText': response}
