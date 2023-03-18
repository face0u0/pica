import lb, numba, math
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(linewidth=1000)

pq1 = (11, 2)
phi_1 = lb.args_index(lb.primitive_root_code(pq1[0], pq1[1], 1), pq1[0])

pq2 = (3, 2)
phi_2 = lb.args_index(lb.primitive_root_code(pq2[0], pq2[1], 1), pq2[0])

k1 = 1
k2 = 2
t0 = 4

print(phi_1)
print(np.roll(phi_1, -t0))

i1 = np.mod(phi_1*k1 - np.roll(phi_1, -t0)*k2, pq1[0])
i2 = np.mod(phi_2*k1 - np.roll(phi_2, -t0)*k2, pq2[0])
s = 0
for v1 in i1:
	for v2 in i2:
		s += v1/pq1[0] + v2/pq2[0]
print(s)