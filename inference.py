import json
from commons import get_model, get_tensor

with open('dog_breed_classes.json') as f:
    classes = json.load(f)

model = get_model()

def get_dog_breed_name(image_bytes):
    tensor = get_tensor(image_bytes)

    output = model(tensor)

    pred = output.argmax(dim=1)

    return classes[pred]