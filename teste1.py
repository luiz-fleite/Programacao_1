import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

a = np.array([1, 2, 3])
print(a)
print(a.ndim)
print(a.size)
print(type(a))

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.ndim)
print(b.size)
print(type(b))

a = np.arange(10)
print(a)

a = np.arange(10).reshape(2, 5)
print(a)

a = np.zeros((3))
b = np.zeros((3, 4))

print(a)
print(b)

m = np.ones((2, 3))
print(m)

m += 1
print(m)

m *= 9
print(m)

m /= 3
print(m)

a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])
c = a * b
print(c)

a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])
c = a / b
print(c)

a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])
c = np.dot(a, b)
print(c)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
type(a)
type(b)

c = np.concatenate((a, b))
d = np.concatenate((b, a))
type(c)
type(d)

print(c)
print(d)

a = np.array(["1", 2, 3])
b = np.array([4, 5, 6])
print(a.dtype)
print(b.dtype)

c = np.concatenate((a, b))
d = np.concatenate((b, a))
print(type(c))
print(type(d))

print(c)
print(d)

a = np.array([1, 2, 3])
print(a.max())
print(a.min())
print(a.mean())
print(a.sum())

rng = default_rng()
aleatorio = rng.integers(10, size=(2, 4))
print(aleatorio)

a = np.array([1, "Joelma", 2, 3, 4, 5, 6, 7, 8])
print(a)
print(type(a[0]))

rng1 = default_rng()
rng2 = default_rng()
rng3 = default_rng()

dados_x = rng1.integers(20, size=30)
dados_y = rng2.integers(12, size=30)
dados_z = rng3.integers(99, size=30)

plt.scatter(x=dados_x, y=dados_y, s=dados_z, c=dados_x)
plt.show()
