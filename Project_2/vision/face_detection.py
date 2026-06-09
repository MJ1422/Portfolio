import cv2
import numpy as np


def detect_face(pil_image):
    """
    Detects the largest face in an image and returns the cropped face.
    """

    # Convert PIL image to NumPy array
    image = np.array(pil_image)

    # Convert RGB to BGR (OpenCV format)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    if len(faces) == 0:
        return None

    # Get the largest face
    largest_face = max(faces, key=lambda face: face[2] * face[3])

    x, y, w, h = largest_face

    face_crop = image[y:y+h, x:x+w]

    # Convert back to RGB
    face_crop = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)

    return face_crop