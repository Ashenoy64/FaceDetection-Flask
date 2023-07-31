# FaceDetection-Flask

Welcome to the FaceDetection-Flask project! This project is a Python Flask-based web application that allows you to upload a video, inspect the frames for detected faces.

## Features

- **Upload Video:** Easily upload a video to the web application for face detection analysis.
- **Inspect Frames:** After uploading a video, click the "Inspect" button to analyze each frame for detected faces and view the results.
- **Standalone Face Detection:** You can also run the face detection script standalone without using the web application.

## How to Run the Web Application

1. Clone the repository from GitHub or download the ZIP file.

   - To clone the repository, open your terminal and run:

     ```bash
     git clone https://github.com/Ashenoy64/FaceDetection-Flask.git
     ```

   - If you downloaded the ZIP file, extract it to a directory of your choice.

2. Navigate to the project directory and install the required dependencies.

   ```bash
   cd FaceDetection-Flask
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   - If you want to run without debug mode, use the following command:

     ```bash
     flask run
     ```

   - If you want to run with debug mode for development, use:

     ```bash
     flask --debug run
     ```

4. The web application will be available at `http://localhost:5000`. You can access it in your web browser.

## Standalone Face Detection

To run the face detection script standalone, follow these steps:

1. Navigate to the `app/videos` directory.

2. Run the `faceDetect.py` script:

   ```bash
   python faceDetect.py
   ```

3.3. The output window will display the video with detected faces highlighted. If that doesn't work, set the `display` parameter to `False` in the `cvDnnDetectFaces` function:

```python
cvDnnDetectFaces(frame, opencv_dnn_model, display=False)
```

In this case, you can view the processed output in the `output.jpg` file instead.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for exploring the FaceDetection-Flask project!