from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

endpoint = "<your_computer_vision_endpoint>"
key = "<your_computer_vision_key>"
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

image_url = "https://example.com/image.jpg"
features = [VisualFeatureTypes.description, VisualFeatureTypes.tags, VisualFeatureTypes.objects]
result = client.analyze_image(image_url, visual_features=features)

for caption in result.description.captions:
    print(f"Description: '{caption.text}' (Confidence: {caption.confidence:.2f})")
print("Tags:", [tag.name for tag in result.tags])
for obj in result.objects:
    print(f"Object: {obj.object_property}, Location: {obj.rectangle}")