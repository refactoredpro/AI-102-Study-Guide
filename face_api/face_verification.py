from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

face_endpoint = "<your_face_api_endpoint>"
face_key = "<your_face_api_key>"
client = FaceClient(face_endpoint, CognitiveServicesCredentials(face_key))

with open("person1.jpg", "rb") as img1, open("person2.jpg", "rb") as img2:
    face1 = client.face.detect_with_stream(img1)[0].face_id
    face2 = client.face.detect_with_stream(img2)[0].face_id
    verify = client.face.verify_face_to_face(face1, face2)
    print("Is Identical:", verify.is_identical, "Confidence:", verify.confidence)