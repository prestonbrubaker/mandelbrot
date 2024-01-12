import time
import random

minX = -1
minY = -1
maxX = 0
maxY = 0

def is_in_mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return False
    return True


while running:
  x = random.uniform(-2, 2)
  y = random.uniform(-2, 2)
  c = complex(x, y)
  in_set = is_in_mandelbrot(c, 1000)
  if(in_set == True):
    in_set = 1
  else:
    in_set = 0
  with open("mand_data.txt", 'a') as file:
    file.write(str(x) + " " + str(y) + " " + str(in_set) + "\n")
