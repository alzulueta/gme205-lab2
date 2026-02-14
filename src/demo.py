from spatial import Point, PointSet

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)

# Invalid point - handle error so script continues (with AI support)
try:
    q = Point("X", 999, 14)  # Invalid longitude
    print(q.id, q.lon, q.lat)
except ValueError as e:
    print("Caught an invalid point:", e)

# ------------------------------------------------------------------
# Test to_tuple() instance method
# ------------------------------------------------------------------

p = Point("A", 121.0, 14.6) 
print(p.id, p.lon, p.lat) 
print(p.to_tuple())

# ------------------------------------------------------------------
# Test distance_to() instance method (with AI support)
# ------------------------------------------------------------------
p1 = Point("A", 121.0, 14.6)
p2 = Point("B", 122.0, 15.0)

distance = p1.distance_to(p2)
print("Distance between p1 and p2:", distance, "meters")

# 4. How did this function return the Haversine value?
# The distance_to() method calculates the shortest distance between two points on Earth
# using their latitude and longitude. It uses the Haversine formula, which accounts
# for the Earth's round shape, and returns the distance in meters.

