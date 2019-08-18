import json
import os

import flask
from flask import request
from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, Date)


blueprint = flask.Blueprint('sqlalchemy', __name__)

engine = create_engine('mysql+pymysql://hacka:admin@localhost/symbal', echo=False)
metadata = MetaData(bind=engine)

user_table = Table('usuario', metadata, Column('id', Integer, primary_key=True), 
                    Column('nome', String(50)),
                    Column('dtnasc', Date)
)
metadata.create_all(engine)

con = engine.connect()

@blueprint.route('/sqlalchemy', methods=[ 'GET' ])
def crudesqlalchemy_insert():
    con.execute("INSERT INTO usuario VALUES(NULL ,'Sarahhhhhh', '1982-05-25')")
    return{'result' : 'Done'}

@blueprint.route('/sqlalchemy', methods=[ 'POST' ])
def crudesqlalchemy_select():
    select = con.execute('SELECT * FROM usuario')
    for item in select:
        print(item)
    
    return{'result' : 'Done'}

