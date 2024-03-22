import os
import torch
import cloudpickle

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

import torch
torch.cuda.is_available()

def load_model(filename):
    map_location = torch.device('cpu')  # Specify CPU as the target device
    
    with open(filename, 'rb') as f:
        model = cloudpickle.load(f)
    
    if torch.cuda.is_available():
        model = model.to(map_location)  # Move the model to the CPU
    
    return model


def chatbot(question, model):
    answer = model({"question":question})
    return answer