# Jane street puzzle
# Single-Cross 2

import numpy as np
import janestreetutil as utl
from scipy.optimize import minimize_scalar

N = 660000  # Number of samples


def p_hat_wrapped(d):  # We just use this wrapping to make optimization easier/cleaner
    return -utl.estimate_p_antithetic(theta, phi, d, starting_vector)


# simulate starting points in the cube
# (0,1)x(0,1)x(0,1)
starting_points_x = np.random.uniform(0, 1, N)
starting_points_y = np.random.uniform(0, 1, N)
starting_points_z = np.random.uniform(0, 1, N)

starting_vector = [starting_points_x, starting_points_y, starting_points_z]

# angle simulation
theta = np.random.uniform(0, np.pi, N)
phi = np.random.uniform(0, 1 / 2 * np.pi, N)

res = minimize_scalar(p_hat_wrapped, method="Brent", tol=0.00000001)

print(res)
