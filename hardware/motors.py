from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice

from config.gpio_config import LEFT_MOTOR
from config.gpio_config import RIGHT_MOTOR


class Motors:

    def __init__(self):

        self.left_enable = PWMOutputDevice(
            LEFT_MOTOR["enable"]
        )

        self.left_in1 = DigitalOutputDevice(
            LEFT_MOTOR["in1"]
        )

        self.left_in2 = DigitalOutputDevice(
            LEFT_MOTOR["in2"]
        )

        self.right_enable = PWMOutputDevice(
            RIGHT_MOTOR["enable"]
        )

        self.right_in1 = DigitalOutputDevice(
            RIGHT_MOTOR["in1"]
        )

        self.right_in2 = DigitalOutputDevice(
            RIGHT_MOTOR["in2"]
        )

        self.speed = 0.75

    def forward(self):

        self.left_in1.on()
        self.left_in2.off()

        self.right_in1.on()
        self.right_in2.off()

        self.left_enable.value = self.speed
        self.right_enable.value = self.speed

    def backward(self):

        self.left_in1.off()
        self.left_in2.on()

        self.right_in1.off()
        self.right_in2.on()

        self.left_enable.value = self.speed
        self.right_enable.value = self.speed

    def left(self):

        self.left_in1.off()
        self.left_in2.on()

        self.right_in1.on()
        self.right_in2.off()

        self.left_enable.value = self.speed
        self.right_enable.value = self.speed

    def right(self):

        self.left_in1.on()
        self.left_in2.off()

        self.right_in1.off()
        self.right_in2.on()

        self.left_enable.value = self.speed
        self.right_enable.value = self.speed

    def stop(self):

        self.left_enable.off()
        self.right_enable.off()

    def cleanup(self):

        self.stop()

        self.left_enable.close()
        self.right_enable.close()

        self.left_in1.close()
        self.left_in2.close()

        self.right_in1.close()
        self.right_in2.close()