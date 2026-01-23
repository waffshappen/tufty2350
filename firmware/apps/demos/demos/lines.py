import random
import math

def update():
  random.seed(0)

  for i in range(100):
    x = math.sin(i + io.ticks / 500) * 40
    y = math.cos(i + io.ticks / 500) * 40
    p1 = vec2(x + bw.rnd(-50, 210), y + bw.rnd(-50, 170))
    p2 = vec2(x + bw.rnd(-50, 210), y + bw.rnd(-50, 170))
    screen.pen = color.rgb(bw.rnd(255), bw.rnd(255), bw.rnd(255))
    screen.line(p1, p2)

