print ("EXERCISE 11.1")
import math
import numpy as np
import matplotlib.pyplot as plt

D, Nx, Nt, L, T = 1.0, 50, 1000, 1.0, 0.1
t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - t[0]
r = D*dt / (dx*dx)
print ( "r = {}".format(r) )
assert r < 0.5

u = np.empty( (Nx+1,Nt+1), dtype=float )  

u[:,0] = 4.0 * x * (1-x)   
u[:,0] = 1.0   

u[0,:] = 0.0
u[Nx,:] = 0.0

for j in range(Nt):
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]

print ( u )
plt.title("1D heat equation")
plt.xlabel("time")
plt.ylabel("x")

plt.imshow(u[:,::5], cmap='jet', interpolation='nearest')

plt.colorbar()
plt.show()

print ("EXERCISE 11.2")

import math
import numpy as np
import matplotlib.pyplot as plt


Nx, Nt, L, T, c = 100, 1000, 1.0, 2.0, 1.0
t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - t[0]
r = (c*dt/dx)**2
print ( "r = {}".format(r) )
assert r < 1

u = np.zeros( (Nx+1,Nt+1), dtype=float )

u[:, 0] = x * (2/3)

u[0,:] = 0.0
u[Nx,:] = 0.0

for j in range(1,Nt):
    u[1:-1,j+1] = -u[1:-1,j-1] +2*u[1:-1,j] + r*(u[:-2,j] -2*u[1:-1,j] + u[2:,j])

plt.title("1D wave equation")
plt.xlabel("t")
plt.ylabel("x")

time_points = [0.0*T, 0.2*T, 0.4*T, 0.6*T, 0.8*T, 1.0*T]

for time in time_points:
    time_index = int(time / T * Nt)
    plt.plot(x, u[:, time_index], label=f"t = {time:.2f}T")

plt.legend()
plt.show()

