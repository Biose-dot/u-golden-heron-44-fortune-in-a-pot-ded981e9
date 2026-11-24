import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = "Dear fern: great sunlight is coming your way, plus one surprise watering from a human who finally remembered you exist."
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
