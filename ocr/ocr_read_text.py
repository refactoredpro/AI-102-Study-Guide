from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time

endpoint = "<your_endpoint>"
key = "<your_key>"
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

image_url = "https://example.com/text-image.jpg"
read_response = client.read(image_url, raw=True)
operation_location = read_response.headers["Operation-Location"]
operation_id = operation_location.split("/")[-1]

while True:
    result = client.get_read_result(operation_id)
    if result.status not in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
        break
    time.sleep(1)

if result.status == OperationStatusCodes.succeeded:
    for page in result.analyze_result.read_results:
        for line in page.lines:
            print(line.text)