import pygame
import time

pygame.init()

window = pygame.display.set_mode((600, 600))

maxW = 600
maxH = 600

pCX = 100
pCY = 100

pSX = maxW / pCX
pSY = maxH / pCY

def is_in_mandelbrot(c, max_iter=100):

    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return False
    return True

#c = complex(0.3, 0.5)
#result = is_in_mandelbrot(c)
#print(f"The number {c} is in the Mandelbrot set: {result}")


window.fill((100, 100, 100))
for y in range(0, pCY):
    for x in range(0, pCX):
        yDisp = y * pSY
        xDisp = x * pSX
        ySet = ((y - pCY) / pCY - 0.5) * 4
        xSet = ((y - pCX) / pCX - 0.5) * 4
        c = complex(xSet, ySet)
        if(is_in_mandelbrot(x, 100) == True):
            pygame.draw.rect(window, (255, 0, 0), (xSet, ySet, pSX, pSY))
        else:
            pygame.draw.rect(window, (0, 0, 0), (xSet, ySet, pSX, pSY))
        

time.sleep(1000)
        
        
