from flask import Blueprint

bp = Blueprint('inspection', __name__)

from app.inspection import routes