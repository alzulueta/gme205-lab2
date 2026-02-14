# GmE 205 Lab 2 Simple Spatial Objects in Python
# How to set up the virtual environment
1. Open the VS Code Terminal
2. Create the virtual environment:
python3 -m venv .venv
3. Activate the environment:
source .venv/bin/activate
4. Install packages:
pip install pandas matplotlib
5. Saved installed packages:
pip freeze > requirements.txt
# How to run Python scripts
1. Make sure the virtual environment is activated ((.venv) shows in the terminal)

## Reflections

1. Modeling points as objects changed the way I thought about the data by giving each point both identity and behavior. Instead of treating points as mere rows in a CSV, each Point now knows its own coordinates, tag, and optional name. This allowed me to directly ask questions like “Is this point a POI?” or “What is the distance to another point?” without having to manipulate raw tables or look up multiple columns manually.
2. The Point manages behaviors intrinsic to a single point, including distance_to() and is_poi(). For PointSet, it manages behaviors at the collection level, such as counting points, computing the bounding box, or filtering points by tag. And lastly, the runner script (run_lab2.py), handles output-related tasks, including visualization and generating JSON summaries. One concrete example is by filtering all POIs is the responsibility of PointSet (filter_by_tag("poi")), not Point, because it operates on a collection, not a single point.
3. Separating geometry, meaning, and behavior improves clarity and maintainability. Geometry is confined to coordinates, meaning is derived from tags and optional attributes, and behavior resides in the appropriate class. This prevents “God objects” and makes it easier to extend functionality while keeping code organized and readable.