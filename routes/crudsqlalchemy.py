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

@blueprint.route('/products', methods=[ 'POST' ])
def crudesqlalchemy_insert():
    
    name = request.form['name']
    description = request.form['description']
    tags = request.form['tags']
    print(name)
    
    con.execute("INSERT INTO products VALUES(NULL ,'"+name+"', '"+tags+"', '"+description+"')")
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
    

@blueprint.route('/newproduct', methods=[ 'GET' ])
def render_new_product():
    context = {
        'title': 'Python | Sysadmin',
        'users': 'Python | Sysadmin',
    }
    return flask.render_template('newproduct.html', context=context)

@blueprint.route('/products', methods=[ 'GET' ])
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

    
