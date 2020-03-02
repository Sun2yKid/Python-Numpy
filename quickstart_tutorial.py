"""
NumPy is the fundamental package for scientific computing with Python. It contains among other things:
* a powerful N-dimensional array object
* sophisticated (broadcasting) functions
* tools for integrating C/C++ and Fortran code
* useful linear algebra, Fourier transform, and random number capabilities
Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data.
Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

refers:
 https://numpy.org/
 https://numpy.org/devdocs/user/quickstart.html
 https://numpy.org/devdocs/reference/index.html#reference
 http://cs231n.github.io/python-numpy-tutorial/
"""

import numpy as np

a = np.arange(15)
print(a, type(a))

a = a.reshape(3, 5)
print(a, type(a))


# Boolean masking
import matplotlib.pyplot as plt

a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a, b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

