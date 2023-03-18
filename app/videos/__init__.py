from flask import Blueprint

bp = Blueprint('videos', __name__)

from app.videos import routes