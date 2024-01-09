#!usr/bin/python3

""" Creates a blueprint"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/vi')

from api.v1.views.index import *
