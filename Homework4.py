print("EXERCISE 4.1")

point_list = [(0, 0), (1, 1), (0.5, -0.5), (3, 2)]
print(point_list)
print("(a)")
circle = lambda p: p[0]**2 + p[1]**2 <= 1
points_circle = list(filter(lambda p: circle(p), point_list))
print(points_circle)

print("(b)")
positive = lambda p: p[0] > 0 and p[1] > 0
points_positive = list(filter(lambda p: positive(p), point_list))
print(points_positive)

print("(c)")
sorting_key_y_decreasing_x_increasing = lambda p: (-p[1], p[0])
point_list.sort(key=lambda p: sorting_key_y_decreasing_x_increasing(p))
print(point_list)

print("(d)")
sorting_key_sum = lambda p: abs(p[0]) + abs(p[1])
point_list.sort(key=lambda p: sorting_key_sum(p))
print(point_list)

print("EXERCISE 4.2")
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L)
print("Iterative case")
def reverse_range_iterative(L, left, right):
    for i in range((right - left + 1) // 2):
        L[left + i], L[right - i] = L[right - i], L[left + i]
reverse_range_iterative(L, 3, 6)
print(L)

print("Recursive case")
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def reverse_range_recursive(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    reverse_range_recursive(L, left + 1, right - 1)

reverse_range_recursive(L, 3, 6)
print(L)  

print("EXERCISE 4.3")

print("(a)")
def iter_even():
    num = 0
    while True:
        yield num
        num += 2
gen = iter_even()
print(next(gen))
print(next(gen))
print(next(gen))

print("(b)")
def iter_odd():
    num = 1
    while True:
        yield num
        num += 2
gen = iter_odd()
print(next(gen))
print(next(gen))
print(next(gen))

print("(c)")
def iter_power(k):
    num = 1
    while True:
        yield num
        num *= k
gen = iter_power(2)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = iter_power(4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
