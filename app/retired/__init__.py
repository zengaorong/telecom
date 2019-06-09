from flask import Blueprint

retired = Blueprint('retired', __name__)

from . import views
