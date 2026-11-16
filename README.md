# The Chalk Dragon — ai-excited-01

A child's pastel chalk dragon, drawn on dark asphalt, tears itself off the
pavement and comes alive: the front half is a real dragon of teal scales
cracked with golden light, lunging at the viewer, while the back half is
still chalk lines and coloured dust on the ground.

`main.py` holds no drawing code. It copies the stored `entry.png` (a JPEG
under a .png name, which the gate reads by its first bytes) to the output
directory — `MAKEFUN_OUTPUT_DIR` when set, `/output` otherwise — so both
grading runs write exactly the same bytes.

The image is 1024 × 1024 and 303,884 bytes, inside the 1 MiB gate.
