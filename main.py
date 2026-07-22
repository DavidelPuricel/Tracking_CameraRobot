import cv2

from web.server import stream, start_server
import threading
from camera.camera import Camera

from vision.face_detector import FaceDetector
from vision.tracker import FaceTracker

from hardware.servo import Servo
from hardware.motors import Motors

from controller.robot_controller import RobotController


def main():

    camera = Camera()

    detector = FaceDetector()

    tracker = FaceTracker(640)

    servo = Servo()

    motors = Motors()

    controller = RobotController()

    threading.Thread(
        target=start_server,
        daemon=True
        ).start()
    

    try:

        while True:

            frame = camera.read()

            if frame is None:
                break

            faces = detector.detect(frame)

            detector.draw(frame, faces)

            face = tracker.get_largest_face(faces)

            error = tracker.calculate_error(face)

            servo.update(error)

            servo_angle = servo.get_angle()

            command = controller.update(
                face,
                servo_angle
            )
            if command == "LEFT":

                motors.left()

            elif command == "RIGHT":

                motors.right()

            elif command == "FORWARD":

                motors.forward()

            elif command == "BACKWARD":

                motors.backward()

            else:

                motors.stop()

            if face is not None:

                x, y, w, h = face

                cv2.putText(
                    frame,
                    f"Command: {command}",
                    (20,30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Error: {error}",
                    (20,60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Face Width: {w}",
                    (20,90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,0),
                    2
                )

            cv2.line(
                frame,
                (320,0),
                (320,480),
                (255,0,0),
                2
            )

            stream.update(frame)

            
    finally:

        motors.cleanup()

        servo.cleanup()

        camera.release()

        



if __name__ == "__main__":

    main()