from inference_sdk import InferenceHTTPClient
import cv2
import json
import os
from dotenv import load_dotenv
from inference_sdk import InferenceHTTPClient
load_dotenv()

api_key = os.getenv("ROBOFLOW_API_KEY")

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=api_key
)

image_path = "sample_test\img4.jpg"
image = cv2.imread(image_path)
result = CLIENT.infer(image, model_id="sudden-infant-death-syndrome/3")
print(result)



output_dir = "results"
output_file = os.path.join(output_dir, "detection_result.json")
with open(output_file, "w") as f:
    json.dump(result, f, indent=4)

print(f"Output saved to {output_file}")