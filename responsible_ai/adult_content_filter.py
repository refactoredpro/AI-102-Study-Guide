from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

endpoint = "<your_endpoint>"
key = "<your_key>"
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

image_url = "https://example.com/sensitive-image.jpg"
features = [VisualFeatureTypes.adult]
result = client.analyze_image(image_url, visual_features=features)

if result.adult.is_adult_content or result.adult.is_racy_content:
    print("Flagged as adult or racy content.")
else:
    print("Image passed content moderation.")