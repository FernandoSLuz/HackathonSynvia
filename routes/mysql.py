import json
import os

import flask
from flask import request

blueprint = flask.Blueprint('mysql', __name__)
@blueprint.route('/mysql_insert', methods=[ 'GET', 'POST' ])
def dialog():
    return {'fulfillmentText': "insert"}
