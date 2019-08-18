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
        prod_Description += ("Digite " + str(jsonList[index+1]["id"]) + " para selecionar" +  str(jsonList[index]["product_name"]) + ".\n\n")
        index = index + 1
    return prod_Description


blueprint = flask.Blueprint('dialog', __name__)
@blueprint.route('/dialog', methods=[ 'GET', 'POST' ])
def dialog():
    print("Passed")
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    str_Products = crudesqlalchemy_select()
    if(res is 'null'):
        print("Passed2")
        return {'fulfillmentText': '404'}
    else:
        intentName = form['queryResult']['intent']['displayName']
        print("Passed3")
        if(str(intentName) == 'op1') :
            print(str_Products)
            return {'fulfillmentText': "Texto digitado: " + str_Products}
        else:
            return {'fulfillmentText': "Intent " + intentName + " not listed on our database"}
