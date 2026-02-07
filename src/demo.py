from spatial import Point

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)

# Invalid point - handle error so script continues (with AI support)
try:
    q = Point("X", 999, 14)  # Invalid longitude
    print(q.id, q.lon, q.lat)
except ValueError as e:
    print("Caught an invalid point:", e)

p = Point("A", 121.0, 14.6) 
print(p.id, p.lon, p.lat) 
print(p.to_tuple())

# ------------------------------------------------------------------
# Test distance_to() method (with AI support)
# ------------------------------------------------------------------
r = Point("B", 121.1, 14.7)
print(f"Distance between {p.id} and {r.id}: {p.distance_to(r):.2f} km")

# ------------------------------------------------------------------
# Test static Haversine method (with AI support)
# ------------------------------------------------------------------
distance_m = Point.haversine_m(121.0, 14.6, 121.1, 14.7)
print(f"Haversine distance: {distance_m:.2f} meters")
# To answer the question in B.7.4: 
# The haversine_m() function finds how far apart two points are on Earth.
# It uses their longitude and latitude and a formula that accounts for the Earth's round shape.
# It gives the distance in meters.





