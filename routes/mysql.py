import json
import os

import flask
from flask import request

blueprint = flask.Blueprint('mysql', __name__)


@blueprint.route('/mysql_insert', methods=[ 'GET', 'POST' ])
def mysql_insert():
    form = request.get_json(silent=True, force=True)
    return {'fulfillmentText': "insert"}

@blueprint.route('/mysql_select', methods=[ 'GET', 'POST' ])
def mysql_select():
    form = request.get_json(silent=True, force=True)
    return {'fulfillmentText': "select"}
