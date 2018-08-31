from numba import vectorize, float64

@vectorize([float64(float64, float64)])
def f(x, y):
    return x + y
