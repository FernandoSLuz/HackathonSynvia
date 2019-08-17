import logging

import flask


blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def sign_in():

    context = {
        'title': 'Python | Sysadmin',
    }
    
    if flask.request.method == 'POST':

        form = flask.request.form
        logging.warning('Falha ao se logar, faltou o código, hihihi')
        
    return flask.render_template('sign-in.html', context=context)