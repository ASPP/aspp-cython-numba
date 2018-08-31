import numpy as np
from numba import jit

data1 = np.linspace(1, 300, 3000).reshape(-1, 120)
data2 = np.linspace(-1, 300, 60000).reshape(120, -1)
print(data1.shape, data2.shape)

out1 = data1 @ data2

def my_dot(x, y):
    assert x.shape[1] == y.shape[0]
    out = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            for k in range(x.shape[1]):
                out[i, j] += x[i, k] * y[k, j]
    return out

out2 = my_dot(data1, data2)

jit_dot = jit(my_dot)
out3 = jit_dot(data1, data2)

jit2_dot = jit(my_dot, parallel=True)
out4 = jit_dot(data1, data2)
