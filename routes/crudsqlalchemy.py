import json
import os
import decimal, datetime

import flask
from flask import request
from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, Date)


blueprint = flask.Blueprint('sqlalchemy', __name__)

engine = create_engine('mysql+pymysql://hacka:admin@localhost/symbal', echo=False)
metadata = MetaData(bind=engine)

metadata.create_all(engine)

con = engine.connect()

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

@blueprint.route('/sqlalchemy', methods=[ 'POST' ])
def crudesqlalchemy_insert():
    con.execute("INSERT INTO products VALUES(NULL ,'Vodka', 'aguardente TOP', 'O NECESSARIO')")
    return{'result' : 200}

@blueprint.route('/sqlalchemy', methods=[ 'GET' ])
def crudesqlalchemy_select():

    selects = con.execute('SELECT * FROM products')
    jsonList = ([dict(r) for r in selects])
    #jsonList = json.loads(dictList)
    #(selects).json()
    print(jsonList)
    context = {
        'title': 'Python | Sysadmin',
        'users': jsonList,
    }
    return flask.render_template('crudsqlalchemy.html', context=context)

    
