import json
import os

import flask
import requests as req
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
        prod_Description += (str(jsonList[index]["id"]) + " - " +  str(jsonList[index]["product_name"])+".\n")
        index = index + 1
    return prod_Description

def getProjects():
    url = 'https://ignixgamestudio-4b7b03.pipedrive.com/v1/deals?api_token=42661dec750e928978d39fb7a1c9d99350616b25'
    commits = req.get(url)
    sales = commits.json()
    index = 0
    prod_Description = ""
    while index < len(sales["data"]):
        prod_Description += ("Job " + str(sales["data"][index]["title"]) + ".\n\nAdicionado em: " + str(sales["data"][index]["add_time"]) +".\n")
        index = index + 1
    return prod_Description


blueprint = flask.Blueprint('dialog', __name__)
@blueprint.route('/dialog', methods=[ 'GET', 'POST' ])
def dialog():
    
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    str_Products = crudesqlalchemy_select()
    if(res is 'null'):
        return {'fulfillmentText': '404'}
    else:
        intentName = form['queryResult']['intent']['displayName']
        if(str(intentName) == 'op1') :
            return {'fulfillmentText': str_Products + "\n\n\nDigite 'Olá' novamente para reiniciarmos o atendimento."}
        elif(str(intentName) == 'op3_fallback'):
            salesName = form['queryResult']['queryText']
            url = 'https://ignixgamestudio-4b7b03.pipedrive.com/v1/deals?api_token=42661dec750e928978d39fb7a1c9d99350616b25'
            data = {
                'title': salesName
                } 
            commits = req.post(url, data = data)
            
            return {'fulfillmentText': "Venda '"+ (form['queryResult']['queryText']) +"' cadastrada com sucesso!\n\n\nDigite 'Olá' novamente para reiniciarmos o atendimento."}
        elif(str(intentName) == 'op4'):
            jobs = getProjects()
            return {'fulfillmentText': jobs}
        else:
            return {'fulfillmentText': "Intent " + intentName + " not listed on our database"}
