import io

import torch
import torch.nn as nn
import torchvision.models as models

from PIL import Image
import torchvision.transforms as transforms

def get_model():
    checkpoint_path = './models/model_checkpoint.pt'
    model = models.resnet50(pretrained=False)
    fc = nn.Linear(2048, 133)
    model.fc = fc
    model.load_state_dict(torch.load(checkpoint_path, map_location='cpu'))
    model.eval()
    return model

def get_tensor(image_bytes):
    image_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    image = Image.open(io.BytesIO(image_bytes))
    return image_transforms(image).unsqueeze(0)

if __name__ == '__main__':
    model = get_model()
    print(model)