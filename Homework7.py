print ("EXERCISE 8.1")

print ("(a)")
import numpy as np
a = np.arange(0.0, 1.1, 0.1, dtype=np.float64)
print(a)

print ("(b)")
b = np.zeros((5, 6), dtype=np.int8)
print(b)

print ("(c)")
x = complex(0, 1)
c = x ** np.arange(9)
print(c)

print ("EXERCISE 8.2")

print ("(a)")
v1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(v1)

print ("(b)")
v2 = v1[1::2]
print(v2)

print ("(c)")
v3 = v1[::-1]
print(v3)

print ("EXERCISE 8.3")
import numpy as np

print ("(a)")
m1 = np.array([[ 1,  2,  3,  4,  5],
               [ 6,  7,  8,  9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])
print(m1)

print ("(b)")
m2 = np.flip(m1, axis=1)
print(m2)

print ("(c)")
m3 = np.flip(m1, axis=0)
print(m3)

print ("(d)")
m4 = m1[1:-1, 1:-1]
print(m4)
