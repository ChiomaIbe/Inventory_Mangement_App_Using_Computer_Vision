from typing import List, Tuple
import cv2
import numpy as np
from edge_impulse_linux.classifier import Classifier

# Load the Edge Impulse model
model = Classifier("path/to/your/model.eim")

def detect_boxes(image: np.ndarray) -> Tuple[int, List[dict]]:
    # Preprocess the image for the model
    processed_image = preprocess_image(image)
    
    # Make predictions using the Edge Impulse model
    predictions = model.classify(processed_image)
    
    box_count = 0
    defected_boxes = []
    
    for prediction in predictions['result']:
        if prediction['label'] == 'box':
            box_count += 1
            if prediction['conf'] < 0.5:  # Assuming a confidence threshold for defect detection
                defected_boxes.append({
                    'label': prediction['label'],
                    'confidence': prediction['conf'],
                    'coordinates': prediction['boundingBox']
                })
    
    return box_count, defected_boxes

def preprocess_image(image: np.ndarray) -> np.ndarray:
    # Resize and normalize the image as required by the model
    image = cv2.resize(image, (224, 224))  # Example size, adjust as needed
    image = image / 255.0  # Normalize to [0, 1]
    return image.astype(np.float32)