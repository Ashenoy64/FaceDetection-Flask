from flask import render_template,redirect,url_for
from app.display import bp



@bp.route('/<filename>')
def display_video(filename):
	#print('display_video filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)