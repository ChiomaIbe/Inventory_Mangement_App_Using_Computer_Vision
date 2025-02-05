class Box:
    def __init__(self, box_id: str, status: str, coordinates: dict):
        self.box_id = box_id
        self.status = status  # 'defected' or 'normal'
        self.coordinates = coordinates  # {'x': float, 'y': float, 'width': float, 'height': float}

    def to_dict(self):
        return {
            "box_id": self.box_id,
            "status": self.status,
            "coordinates": self.coordinates
        }