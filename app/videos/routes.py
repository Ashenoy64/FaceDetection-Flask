import os
from flask import render_template,redirect,request,flash,url_for
from app.videos import bp
from faceDetect import cvDnnDetectFaces
import cv2
import io
from PIL import Image  


def recognizeFace(frameNumber,filename):
    facesDetected=[] 
    opencv_dnn_model = cv2.dnn.readNetFromCaffe(prototxt="models/deploy.prototxt",
                                            caffeModel="models/res10_300x300_ssd_iter_140000_fp16.caffemodel")
    video=cv2.VideoCapture(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads',filename)))
    no=0
    while video.isOpened():
        ret,frame=video.read()
        if ret and no==frameNumber:
            results,facesDetected=cvDnnDetectFaces(frame, opencv_dnn_model, display=False)
        else:
            break
        no+=1
    return facesDetected
    

def encodeImages(faceDetected):
    faceData=[]
    for i in faceDetected:
        img=Image.fromarray(i)
        faceData.append(img)
    return faceData


@bp.route('/<filename>',methods=['POST','GET'])
def display_video(filename):
    files=os.listdir(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads')))
    if request.method=='POST':
        frameNumber=request.form.get('frameNumber')
        faceData=encodeImages(recognizeFace(frameNumber,filename))
        return render_template('videos/videos.html',files=files,filename=filename,faceData=faceData)
    else:
        return render_template('videos/videos.html',files=files,filename=filename)

@bp.route("/")
def display_all():
    files=os.listdir(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads')))
    return render_template('videos/videos.html',files=files)


