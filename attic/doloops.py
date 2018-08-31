import dis
import numba

@numba.jit
def doloops(n):
    acc = 0
    for i in range(n):
        acc += 1
        if n == 10:
            break
    return acc

@numba.jit
def add(a, b):
    return a + b

#doloops(3)

#dis.dis(add)
#add(1, 5)


@numba.jit
def f(x):
   if x == 0:
      raise ValueError("x cannot be zero")

dis.dis(f)
f(5)
