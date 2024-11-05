import numpy as np

recipe = [ [10.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
p = np.array([1, 1.5, 1, 3, 7])
q = np.array([20.1, 19.9, 10, 5, 5])

R_q = np.array(recipe)
R_p = R_q.copy().T

oversupply = R_q.dot(q)
print(oversupply)
oversupply[0] = 100

print(R_p, R_q, p, q, oversupply)