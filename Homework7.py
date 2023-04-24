print ("EXERCISE 7.1")
def find_axis(v1, v2):
    
    v3 = [v1[1]*v2[2] - v1[2]*v2[1],
          v1[2]*v2[0] - v1[0]*v2[2],
          v1[0]*v2[1] - v1[1]*v2[0]]

    if sum([abs(x) for x in v3]) == 0:
        raise ValueError("vectors are parallel")

    v3_normalize = sum([x**2 for x in v3])**0.5

    v3_unit_vector = [x/v3_normalize for x in v3]

    return v3_unit_vector

v = [-1, 2, -3]
w = [3, -1, 2]

v3 = find_axis(v, w)
print(v3)

print ("EXERCISE 7.2")
print("(a)infinite iterator returning 0, 1, 0, 1, 0, 1, ...")

def zero_one_alternately():
    while True:
        yield 0
        yield 1
a = zero_one_alternately()

print(next(a))
print(next(a))
print(next(a))
print(next(a))

print("(b)infinite iterator returning randomly 0 or 1 on demand")

import random

def zero_one_randomly():
    while True:
        yield random.randint(0, 1)

b = zero_one_randomly()

print(next(b))
print(next(b))
print(next(b))
print(next(b))

print("(c)infinite iterator returning 0, 1, 0, -1, 0, 1, 0, -1, ...")

def zero_one_negative_one():
    values = [0, 1, 0, -1]
    while True:
        for value in values:
            yield value

c = zero_one_negative_one()

print(next(c))
print(next(c))
print(next(c))
print(next(c))
