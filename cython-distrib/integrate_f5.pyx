cdef double f5(double x):
    y = (x*x*x - 3)*x
    return y

def integrate_f5(double a, double b, int n):
    cdef:
        double dx = (b - a) / n
        double dx2 = dx / 2
        double s = f5(a) * dx2
        int i = 0
    for i in range(1, n):
        s += f5(a + i * dx) * dx
    s += f5(b) * dx2
    return s

print(integrate_f5(-100, 100, 100_000))
