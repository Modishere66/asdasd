import torch
import cv2
import numpy as np
from torchvision.transforms import ToTensor

class DepthRefinement:
    def __init__(self):
        self.model = torch.hub.load('intel-isl/MiDaS', 'MiDaS')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        self.model.eval()

    def complete_depth(self, depth_map):
        input_tensor = ToTensor()(depth_map).unsqueeze(0).to(self.device)
        with torch.no_grad():
            depth_map_refined = self.model(input_tensor)
        depth_map_refined = depth_map_refined.squeeze().cpu().numpy()
        return depth_map_refined