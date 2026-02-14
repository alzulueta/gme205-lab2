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