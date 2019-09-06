from flask import Blueprint

activation = Blueprint('activation', __name__)

from . import views
