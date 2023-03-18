import os
from flask import render_template,redirect,request,flash
from app.upload import bp
from werkzeug.utils import secure_filename


@bp.route('/')
def upload_form():
	return render_template('upload/upload.html')

@bp.route('/post', methods=['POST'])
def upload_video():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	else:
		filename = secure_filename(file.filename)
		file.save(os.path.join('app/static/uploads/', filename))
		#print('upload_video filename: ' + filename)
		flash('Video successfully uploaded and displayed below')
		return render_template('upload/upload.html', filename=filename)
