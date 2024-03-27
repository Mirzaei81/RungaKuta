from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
v0= 10
k = 0.23
def f(v,ca):
    ra  = -k*ca 
    return ra/v0
vspan=[0,100]
ca0  =[10]
sol = solve_ivp(f,vspan,ca0)
print(sol.y)
vSpan = np.linspace(0,0.1,100)
plt.plot(vSpan, sol.y.T)
plt.xlabel('Ca')
plt.ylabel('Solution')
plt.title('Solution of IVP')
plt.show()
print(sol.t)
print(sol.y[0])
