from app.face_detection import FaceDetector

face_detector = FaceDetector()

def test_find_faces_in_images():
    assert face_detector.find_faces('mocks/felipmartins_image.jpg') == True
    assert face_detector.find_faces('mocks/asdf_image.jpg') == False

def test_find_faces_with_no_images():
    assert face_detector.find_faces('') == False
    assert face_detector.find_faces(None) == False