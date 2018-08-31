import numpy as np
from numba import cfunc
def integrand(t):
    return np.exp(-t) / t**2

nb_integrand = cfunc("float64(float64)")(integrand)

import scipy.integrate as si
def do_integrate(func):
    """
    Integrate the given function from 1.0 to +inf.
    """
    return si.quad(func, 1, np.inf)

# >>> do_integrate(integrand)
# (0.14849550677592208, 3.8736750296130505e-10)
# >>> do_integrate(nb_integrand.ctypes)
# (0.14849550677592208, 3.8736750296130505e-10)

# >>> %timeit do_integrate(integrand)
# 1000 loops, best of 3: 242 µs per loop
# >>> %timeit do_integrate(nb_integrand.ctypes)
# 100000 loops, best of 3: 13.5 µs per loop
