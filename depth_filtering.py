import cv2
import numpy as np

def apply_filters(depth_map):
    # Apply bilateral filter
    depth_map_filtered = cv2.bilateralFilter(depth_map, 9, 75, 75)
    # Apply median filter
    depth_map_filtered = cv2.medianBlur(depth_map_filtered, 5)
    return depth_map_filtered