# Load and run the model:

from transformers import pipeline
from PIL import Image

pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

image_path = "C:/Users/Lenovo/OneDrive/Desktop/Highlevel.png"
image = Image.open(image_path)

caption = pipe(image)
print(caption)  