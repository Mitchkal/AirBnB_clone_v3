#!/usr/bin/python3
<<<<<<< HEAD
"""
app
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

=======
"""module app.py"""

from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
>>>>>>> 91652a45b459eeeddd244b96a625b39a7fead9ac
app.register_blueprint(app_views)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown(exception):
    """
    teardown function
    """
=======
def teardown_appcontext(exception):
>>>>>>> 91652a45b459eeeddd244b96a625b39a7fead9ac
    storage.close()


@app.errorhandler(404)
<<<<<<< HEAD
def handle_404(exception):
    """
    handles 404 error
    :return: returns 404 json
    """
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return(resp)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
=======
def not_found_error(error):
    """handles 404 errors"""
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    # response.headers['Connection'] = 'close'
    return response


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
>>>>>>> 91652a45b459eeeddd244b96a625b39a7fead9ac
