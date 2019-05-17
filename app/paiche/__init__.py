from flask import Blueprint

paiche = Blueprint('paiche', __name__)

from . import views
