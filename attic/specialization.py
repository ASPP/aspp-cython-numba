from numba import jit, int32

@jit(int32(int32, int32))
def f(x, y):
    # A somewhat trivial example
    return x + y

print(f)

# print(f(123, 123**30))


@jit(nopython=True)
def f(x, y):
    return x + y
