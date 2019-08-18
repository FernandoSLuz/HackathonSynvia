import json
import os

import flask
from flask import request
from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, Date)

engine = create_engine('mysql+pymysql://hacka:admin@localhost/symbal', echo=False)

metadata = MetaData(bind=engine)

metadata.create_all(engine)

con = engine.connect()

def crudesqlalchemy_select():
    selects = con.execute('SELECT * FROM products')
    jsonList = ([dict(r) for r in selects])
    index = 0
    prod_Description = ""
    while index < len(jsonList):
        prod_Description += str(index) + "\n"
    return prod_Description


blueprint = flask.Blueprint('dialog', __name__)
@blueprint.route('/dialog', methods=[ 'GET', 'POST' ])
def dialog():
    
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    print("Request:" + res)
    str_Products = crudesqlalchemy_select()
    if(res is 'null'):
        return {'fulfillmentText': str_Products}
    else:
        responseText = ''
        intentName = form['queryResult']['intent']['displayName']
        if(str(intentName) == 'op1') :
            responseText = form['queryResult']['queryText']
            return {'fulfillmentText': "Texto digitado: " + responseText}
        else:
            return {'fulfillmentText': "Intent " + intentName + " not listed on our database"}
