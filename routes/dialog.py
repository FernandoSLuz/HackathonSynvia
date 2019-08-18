import json
import os

import flask
from flask import request


blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/dialog', methods=[ 'GET', 'POST' ])
def dialog():
    
    req = request.get_json(silent=True, force=True)

    print("Request:")
    res = (json.dumps(req, indent=4))
    
    return {'users': res}
