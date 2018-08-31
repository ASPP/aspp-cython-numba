"""
This file uses Python type annotations as Cython type annotations.

It works to some extent, but currently Cython has only partial support
for this syntax, and function visibility cannot be specified. The
resulting code is much slower than the version annotatated using
cython-specific constructs such as cdef.

The advantage is that this is normal Python code.
"""

def f5a(x: float) -> float:
    y = (x*x*x - 3)*x
    return y

def integrate_f5a(a: float, b: float, n: int):
    dx: double = (b - a) / n
    dx2: double = dx / 2
    s: double = f5a(a) * dx2
    i: int = 0
    for i in range(1, n):
        s += f5a(a + i * dx) * dx
    s += f5a(b) * dx2
    return s

# check whether we are using the compiled extension
print(integrate_f5a) # this prints <function integrate_f5a at 0x...> in pure-python mode
                     # and <cyfunction integrate_f5a at 0x...> with a compiled extension

print(integrate_f5a(-100, 100, 100_000))
