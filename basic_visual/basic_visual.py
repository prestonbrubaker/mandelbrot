import pygame
import time

pygame.init()

# Window dimensions
maxW = 800
maxH = 800
window = pygame.display.set_mode((maxW, maxH))

# Plotting dimensions
pCX = 800
pCY = 800

pSX = maxW / pCX
pSY = maxH / pCY

minX = -1
minY = -1
maxX = 0
maxY = 0

def is_in_mandelbrot(c, max_iter=100):
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return False
    return True

window.fill((100, 100, 100))

for y in range(pCY):
    for x in range(pCX):
        # Convert pixel coordinate to complex number
        xSet = x / pCX * (maxX - minX) + minX
        ySet = y / pCY * (maxY - minY) + minY
        c = complex(xSet, ySet)

        # Check if the complex number is in the Mandelbrot set
        if is_in_mandelbrot(c, 100):
            color = (255, 255, 255)  # White for points in the set
        else:
            color = (0, 0, 0)       # Black for points not in the set

        # Draw the point
        pygame.draw.rect(window, color, (x * pSX, y * pSY, pSX, pSY))

# Update the display
pygame.display.flip()

# Keep the window open until it is closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
