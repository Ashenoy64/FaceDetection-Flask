import os
from flask import render_template,redirect,request,flash,url_for
from app.videos import bp

@bp.route('/<filename>')
def display_video(filename):
    files=os.listdir(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads')))
    print(filename)
    return render_template('videos/videos.html',files=files,filename=filename)

@bp.route("/")
def display_all():
    files=os.listdir(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads')))
    return render_template('videos/videos.html',files=files)


