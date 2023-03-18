from flask import Blueprint

bp = Blueprint('display', __name__)


from app.display import routes
