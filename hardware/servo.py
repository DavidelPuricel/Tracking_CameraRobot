from gpiozero import AngularServo

from config.gpio_config import SERVO_PIN


class Servo:

    def __init__(self):

        self.servo = AngularServo(

            SERVO_PIN,

            min_angle=-90,

            max_angle=90

        )

        self.angle = 0

        self.kp = 0.08

    def update(self, error):

        if error is None:
            return

        self.angle -= error * self.kp

        self.angle = max(-90, min(90, self.angle))

        self.servo.angle = self.angle

    def get_angle(self):

        return self.angle

    def center(self):

        self.angle = 0

        self.servo.angle = 0

    def cleanup(self):

        self.center()

        self.servo.close()