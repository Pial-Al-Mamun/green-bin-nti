import cv2
import threading
from app.error import CameraNotFoundError


class _Camera:
    """
    A class to handle video capture from a camera.
    """

    def __init__(self, url: str | int = 0) -> None:
        """
        Initialize the camera.

        :param camera_index: Index of the camera to use.
        """
        self.cap = cv2.VideoCapture(url)

        if not self.cap.isOpened():
            raise CameraNotFoundError

        self.lock = threading.Lock()

    def get_frame(self) -> bytes:
        """
        Capture a frame from the camera.

        :return: JPEG encoded image bytes.
        """
        with self.lock:
            ret, frame = self.cap.read()
            if not ret:
                return b""

            ret, jpeg = cv2.imencode(".jpg", frame)
            if not ret:
                return b""

            return jpeg.tobytes()

    def release(self) -> None:
        """
        Release the camera resource.
        """
        with self.lock:
            if self.cap.isOpened():
                self.cap.release()


# singleton for the camera class
camera = _Camera()
