class FaceTracker:

    def __init__(self, frame_width):

        self.frame_center = frame_width // 2

    def get_largest_face(self, faces):

        if len(faces) == 0:
            return None

        return max(
            faces,
            key=lambda face: face[2] * face[3]
        )

    def calculate_error(self, face):

        if face is None:
            return None

        x, y, w, h = face

        face_center = x + w // 2

        error = face_center - self.frame_center

        return error

    def get_face_width(self, face):

        if face is None:
            return 0

        return face[2]