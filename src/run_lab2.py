from spatial import PointSet

# ------------------------------------------------------------------
# Part C: Usage Check (with AI support)
# ------------------------------------------------------------------

ps = PointSet.from_csv("data/points.csv")
print("Number of points:", ps.count())
print("Bounding box:", ps.bbox())

pois = ps.filter_by_tag("poi")
print("POIs in PointSet:", [p.id for p in pois.points])
print("Number of POIs:", pois.count())

# ------------------------------------------------------------------
# Part D: Challenge Exercise (with AI support)
# ------------------------------------------------------------------

import os
import json
import matplotlib.pyplot as plt

bbox = ps.bbox()
print("Bounding box (min_lon, min_lat, max_lon, max_lat):", bbox)

pois = ps.filter_by_tag("poi")
print("POIs in PointSet:", [p.id for p in pois.points])
print("Number of POIs:", pois.count())

x = [p.lon for p in ps.points]
y = [p.lat for p in ps.points]

plt.figure(figsize=(8,6))
plt.scatter(x, y, color="blue")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("PointSet Scatter Plot")
plt.grid(True)

os.makedirs("output", exist_ok=True)

plt.savefig("output/lab2_preview.png")
plt.close()

tag_counts = {}
for p in ps.points:
    tag = p.tag or "undefined"
    tag_counts[tag] = tag_counts.get(tag, 0) + 1

summary = {
    "total_points": ps.count(),
    "bounding_box": {
        "min_lon": bbox[0],
        "min_lat": bbox[1],
        "max_lon": bbox[2],
        "max_lat": bbox[3]
    },
    "counts_per_tag": tag_counts
}

with open("output/lab2_report.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=4)

print("Visualization saved to output/lab2_preview.png")
print("Summary report saved to output/lab2_report.json")