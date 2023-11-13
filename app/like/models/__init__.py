from flask import Blueprint

consulta_bp = Blueprint('consulta', __name__)

from . import consultas