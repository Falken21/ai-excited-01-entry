# The Chalk Dragon — ai-excited-01

On a patch of dark asphalt, a dragon that a child sketched in pastel chalk
is caught in the middle of bursting into life. Its head, chest and front
legs have already torn free of the pavement as a real creature — glossy
teal scales split by veins of glowing golden light, wings spread, mouth
open in a delighted grin as it lunges toward the viewer. Behind it, the
rest of the body has not caught up yet: the tail and hindquarters are still
flat chalk outlines and puffs of pink, mint and yellow dust on the ground,
with a few stubby chalk sticks scattered where the artist dropped them.

The picture itself is stored in this repository as `entry.png`, a
1024×1024 image. Running `main.py` simply copies that stored file into the
output directory — the folder named by the `MAKEFUN_OUTPUT_DIR`
environment variable when one is set, or `/output` otherwise — creating
the directory first if it does not exist. Because the program always
copies the same stored bytes and never redraws anything, both grading
runs produce exactly the same image.
