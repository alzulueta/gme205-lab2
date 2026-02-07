class Point:
    def __init__(self, id, lon, lat):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        
        if not (-90 <- lat <= 90):
            