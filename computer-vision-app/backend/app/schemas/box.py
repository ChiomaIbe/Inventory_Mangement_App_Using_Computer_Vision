from pydantic import BaseModel
from typing import List, Optional

class BoxSchema(BaseModel):
    box_id: str
    status: str  # e.g., "defected" or "normal"
    coordinates: List[float]  # e.g., [x_min, y_min, x_max, y_max]

class BoxResponseSchema(BaseModel):
    total_boxes: int
    defected_boxes: int
    boxes: List[BoxSchema]

class BoxCountSchema(BaseModel):
    total_boxes: int
    defected_boxes: int