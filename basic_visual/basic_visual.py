def is_in_mandelbrot(c, max_iter=100):

    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return False
    return True

c = complex(0.3, 0.5)
result = is_in_mandelbrot(c)
print(f"The number {c} is in the Mandelbrot set: {result}")
