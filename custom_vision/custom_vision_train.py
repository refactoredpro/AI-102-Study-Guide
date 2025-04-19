from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

training_endpoint = "<your_training_endpoint>"
training_key = "<your_training_key>"
prediction_endpoint = "<your_prediction_endpoint>"
prediction_key = "<your_prediction_key>"

train_credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(training_endpoint, train_credentials)

project = trainer.create_project("SampleProject")
tag1 = trainer.create_tag(project.id, "Tag1")
# Add image upload and training logic here
print("Project and tag created.")