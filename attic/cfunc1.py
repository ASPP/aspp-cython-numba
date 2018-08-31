import numba
import ctypes

@numba.cfunc("float64(float64, float64)")
def add(x, y):
    return x + y

libc = ctypes.cdll.LoadLibrary('libc.so.6')
IntArray5 = ctypes.c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)
qsort = libc.qsort

c_sig = numba.types.intc(numba.types.CPointer(numba.types.intc),
                         numba.types.CPointer(numba.types.intc))
@numba.cfunc(c_sig)
def callback(inta, intb):
    arr_a = numba.carray(inta, (1,))
    arr_b = numba.carray(intb, (1,))
    return arr_a[0] - arr_b[0]
