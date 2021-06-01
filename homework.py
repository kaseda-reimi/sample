import numpy as np
import matplotlib.pyplot as plt

tsp = 3e-9
G = 1e-6
N0 = 2e18
tph = 1e-12
b = np.array([[1e-5], [1e-2], [1e-1], [0.5]])

R = np.linspace(25, 29, 100)

Ne = (-tsp*G*R-1/tph+G*(b-1)*N0)/(2*G*(b-1))


plt.figure(0)
plt.plot(R, Ne[0])
plt.plot(R, Ne[1])
plt.xlabel('log10(R)')
plt.ylabel('Ne')
plt.legend(["β=1e-5", "β=1e-2"])
plt.savefig("Ne.png")
