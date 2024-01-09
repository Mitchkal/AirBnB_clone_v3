<<<<<<< HEAD
#!usr/bin/python3

""" Creates a blueprint"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/vi')

from api.v1.views.index import *
=======
#!/usr/bin/python3

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
>>>>>>> 91652a45b459eeeddd244b96a625b39a7fead9ac
