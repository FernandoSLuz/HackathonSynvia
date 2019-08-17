import sys
import os
import time

import flask
import requests

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET', 'POST' ])
def gitlab():
    headers = {
        'Private-Token': 'pQyP9oUuy-wsEwj1VJWf'
    }
    res_1 = requests.get('http://localhost:8000/api/v4/users', headers=headers)
    users = res_1.json() if res_1.status_code == 200 else []

    res_2 = requests.get('http://localhost:8000/api/v4/projects', headers=headers)
    projects = res_2.json() if res_2.status_code == 200 else []

    print("Test---->" + str(projects))
    #Teste doido
    context = {
        'title': 'Python | Sysadmin',
        'users': users,
        'projects': projects
    }
    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<projectid>', methods=[ 'GET', 'POST' ])
def get_commits(projectid):

    url = 'http://localhost:8000/api/v4/projects/{}/repository/commits'.format(projectid)

    commits = requests.get(url, headers={
        'Private-Token': 'pQyP9oUuy-wsEwj1VJWf'
    })

    context = {
        'title':'Python | Sysadmin',
        'commits': commits.json() if commits.status_code == 200 else []
    }

    return flask.render_template('gitlab_commits.html', context=context)
