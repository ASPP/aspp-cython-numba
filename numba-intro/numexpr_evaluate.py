# numexpr_evaluate.py
import numpy as np, numexpr as ne
a = np.arange(1e6)
b = np.random.randint(10, size=(1_000_000,))
print(ne.evaluate('a*b-4.1*a > 2.5*b'))
