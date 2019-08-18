import json
import os

import flask
from flask import request


blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/dialog', methods=[ 'GET', 'POST' ])
def dialog():
    
    req = request.get_json(silent=True, force=True)


    res = (json.dumps(req, indent=4))
    print("Request:" + res)
    return {
        "speech": res,
        "displayText": "testeeee",
        #"data": {},
        #"contextOut": [],
        "source": "BankRates"
    }
