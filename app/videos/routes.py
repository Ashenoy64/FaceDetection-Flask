import os
from flask import render_template,redirect,request,flash,url_for
from app.videos import bp
import cv2
import io
from PIL import Image  
import dlib
from time import time
import base64
facesDetected=[] 
opencv_dnn_model = cv2.dnn.readNetFromCaffe(prototxt=os.path.realpath(os.path.join(os.path.dirname(__file__), 'models','deploy.prototxt')),caffeModel=os.path.realpath(os.path.join(os.path.dirname(__file__), 'models','res10_300x300_ssd_iter_140000_fp16.caffemodel')))
def cvDnnDetectFaces(image, opencv_dnn_model, min_confidence=0.3, display = True):
    
    image_height, image_width, _ = image.shape

    output_image = image.copy()

    preprocessed_image = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(300, 300),
                                               mean=(104.0, 117.0, 123.0), swapRB=False, crop=False)

    opencv_dnn_model.setInput(preprocessed_image)

    start = time()

    results = opencv_dnn_model.forward()    

    end = time()
        
    
    for face in results[0][0]:
        
        face_confidence = face[2]
        
        if face_confidence > min_confidence:

            bbox = face[3:]

            x1 = int(bbox[0] * image_width)
            y1 = int(bbox[1] * image_height)
            x2 = int(bbox[2] * image_width)
            y2 = int(bbox[3] * image_height)

            facesDetected.append(output_image[y1:y2, x1:x2])
            cv2.rectangle(output_image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=image_width//200)

            cv2.rectangle(output_image, pt1=(x1, y1-image_width//20), pt2=(x1+image_width//16, y1),
                          color=(0, 255, 0), thickness=-1)

            cv2.putText(output_image, text=str(round(face_confidence, 1)), org=(x1, y1-25), 
                        fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=image_width//700,
                        color=(255,255,255), thickness=image_width//200)

    if display:
        
        cv2.putText(output_image, text='Time taken: '+str(round(end - start, 2))+' Seconds.', org=(10, 65),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=image_width//700,
                    color=(0,0,255), thickness=image_width//500)
        
        for i in facesDetected:

            cv2.imwrite('output{}.jpg'.format(facesDetected.index(i)), i)
        
        
    else:
        for i in facesDetected:
            try:
                cv2.imwrite('output.jpg',i)
            except:
                pass
        return results, facesDetected

    





def recognizeFace(frameNumber,filename):
    facesDetected=[] 
    video=cv2.VideoCapture(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads',filename)))
    no=0
    while video.isOpened():
        ret,frame=video.read()

        if no==frameNumber:
            print("entered")
            results,facesDetected=cvDnnDetectFaces(frame, opencv_dnn_model, display=False)
           
            return facesDetected
        no+=1
    
    return facesDetected
    

def encodeImages(faceDetected):
    faceData=[]
    for i in faceDetected:
        try:
            color_coverted = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
            im=Image.fromarray(color_coverted)
            data=io.BytesIO()
            im.save(data,"JPEG")
            encode_img_data=base64.b64encode(data.getvalue())
            faceData.append(encode_img_data.decode())
        except:
            pass
    return faceData


@bp.route('/<filename>',methods=['POST','GET'])
def display_video(filename):
    files=os.listdir(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads')))
    if request.method=='POST':
        frameNumber=request.form['data']

        facesDetected=recognizeFace(int(frameNumber),filename)

        print(facesDetected)
        faceData=encodeImages(facesDetected)
        print(faceData,"Done")
        return render_template('videos/videos.html',files=files,filename=filename,faceData=faceData)
    
    return render_template('videos/videos.html',files=files,filename=filename)

@bp.route("/")
def display_all():
    files=os.listdir(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static','uploads')))
    return render_template('videos/videos.html',files=files)


