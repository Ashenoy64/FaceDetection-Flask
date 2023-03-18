from flask import render_template,request
from app.inspection import bp


@bp.route('/')
def inspect_video():
 pass