import sys
import os
import time

import flask
import requests

from routes.gitlab import blueprint as gitlab_blueprint

#logging.basicConfig(filename="/tmp/app.log",
#        level=logging.DEBUG,
#        format="%(asctime)s - %(levelname)s - %(name)s\
#                %(funcName)s - %(filename)s:%(lineno)s - %(message)s",
#        datefmt="%Y-%m-%d %H:%M:%S")

app = flask.Flask(__name__)
app.debug = True

@app.route('/')
def index():

    res = requests.get('https://gen-net.herokuapp.com/api/users/')
    
    users = res.json() if res.status_code == 200 else []

    def extract(u):
        return u

    context = {
        'title': 'Python | Sysadmin',
        'users': [ extract(u) for u in users ]
    }

    return flask.render_template('index.html', context=context)

if __name__ == "__main__":

    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)

    app.run(host='0.0.0.0')
