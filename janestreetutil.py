import numpy as np


def create_vector(
    theta, phi, d
):  # creates a vector starting at the origin with specified angles and length
    x = d * np.cos(phi) * np.cos(theta)
    y = d * np.cos(phi) * np.sin(theta)
    z = d * np.sin(phi)
    return [x, y, z]


def create_final_vector(
    theta, phi, d, starting_vector
):  # pretty much just adds starting point and vector with random direction.
    vec = create_vector(theta, phi, d)
    fin_vec = np.add(vec, starting_vector)

    return fin_vec


def antithetic(vector):  # creates the antithetic samples of he input vector
    x = 1 - vector[0] + 0.5
    y = 1 - vector[1] + 0.5
    z = 1 - vector[2] + 0.5

    return [x, y, z]


def estimate_p_antithetic(
    theta, phi, d, starting_vector
):  # creates a vector and give p_hat using antithetic sampling
    N = len(theta)
    final_vector = create_final_vector(theta, phi, d, starting_vector)
    final_vector_antithetic = antithetic(final_vector)

    bool_vector = check_if_endpoint_orthogonal(final_vector)
    bool_vector_antithetic = check_if_endpoint_orthogonal(final_vector_antithetic)

    p_hat = ((bool_vector.sum() / N) + (bool_vector_antithetic.sum() / N)) / 2
    return p_hat


def box_1(starting_vector):
    l = (
        (starting_vector[1] > 0)
        & (starting_vector[1] < 1)
        & (starting_vector[2] > 0)
        & (starting_vector[2] < 1)
        & (starting_vector[0] > 1)
        & (starting_vector[0] < 2)
    )
    return l


def box_2(starting_vector):
    l = (
        (starting_vector[1] > 0)
        & (starting_vector[1] < 1)
        & (starting_vector[2] > 0)
        & (starting_vector[2] < 1)
        & (starting_vector[0] < 0)
        & (starting_vector[0] > -1)
    )
    return l


def box_3(starting_vector):
    l = (
        (starting_vector[1] < 0)
        & (starting_vector[1] > -1)
        & (starting_vector[2] > 0)
        & (starting_vector[2] < 1)
        & (starting_vector[0] > 0)
        & (starting_vector[0] < 1)
    )
    return l


def box_4(starting_vector):
    l = (
        (starting_vector[1] > 1)
        & (starting_vector[1] < 2)
        & (starting_vector[2] > 0)
        & (starting_vector[2] < 1)
        & (starting_vector[0] < 1)
        & (starting_vector[0] > 0)
    )
    return l


def box_5(starting_vector):
    l = (
        (starting_vector[1] > 0)
        & (starting_vector[1] < 1)
        & (starting_vector[2] > 1)
        & (starting_vector[2] < 2)
        & (starting_vector[0] < 1)
        & (starting_vector[0] > 0)
    )
    return l


def box_6(starting_vector):
    l = (
        (starting_vector[1] > 0)
        & (starting_vector[1] < 1)
        & (starting_vector[2] > -1)
        & (starting_vector[2] < 0)
        & (starting_vector[0] < 1)
        & (starting_vector[0] > 0)
    )
    return l


def check_if_endpoint_orthogonal(vector):
    res = (
        box_1(vector)
        | box_2(vector)
        | box_3(vector)
        | box_4(vector)
        | box_5(vector)
        | box_6(vector)
    )
    return res
