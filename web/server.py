from flask import Flask, Response, render_template
import cv2
import threading


app = Flask(
    __name__,
    template_folder="templates"
)


class VideoStream:

    def __init__(self):
        self.frame = None
        self.lock = threading.Lock()


    def update(self, frame):

        with self.lock:
            self.frame = frame.copy()


    def get_frame(self):

        with self.lock:

            if self.frame is None:
                return None

            return self.frame.copy()



stream = VideoStream()



@app.route("/")
def index():

    return render_template(
        "index.html"
    )



def generate_frames():

    while True:

        frame = stream.get_frame()

        if frame is None:
            continue


        success, buffer = cv2.imencode(
            ".jpg",
            frame
        )


        if not success:
            continue


        frame_bytes = buffer.tobytes()


        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame_bytes
            + b"\r\n"
        )



@app.route("/video")
def video():

    return Response(
        generate_frames(),
        mimetype=
        "multipart/x-mixed-replace; boundary=frame"
    )



def start_server():

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        threaded=True
    )