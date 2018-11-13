from PIL import Image
from basic_robot.camera import Camera


cam = Camera()
img = cam.update()

width, height = img.size
col = [0, 0, 0]
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        col[0] += r
        col[1] += g
        col[2] += b

tot = sum(col)
frac = [c / tot for c in col]
print(frac)
