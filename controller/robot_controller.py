class RobotController:

    def __init__(self):

        self.turn_threshold = 35

        self.target_face_width = 170

        self.distance_threshold = 20

    def update(self, face, servo_angle):

        if face is None:
            return "STOP"

        #
        # Dacă servo-ul este mult rotit,
        # robotul se aliniază.
        #

        if servo_angle < -self.turn_threshold:
            return "LEFT"

        if servo_angle > self.turn_threshold:
            return "RIGHT"

        #
        # Servo-ul este aproape centrat.
        # Acum controlăm doar distanța.
        #

        _, _, w, _ = face

        if w < self.target_face_width - self.distance_threshold:
            return "FORWARD"

        if w > self.target_face_width + self.distance_threshold:
            return "BACKWARD"

        return "STOP"