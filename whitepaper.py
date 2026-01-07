# 100% vibe coded white paper script

from PIL import Image

# A4 at 300 DPI
W, H = 2480, 3508

img = Image.new("RGB", (W, H), "white")
img.save("a4_white.png")

