import numpy as np

def basis(robots, icecreams):
    """
    basis function phi

    @param robots: (N,) grid position of robots
    @param icecream: (M,) grid position of icecream shops
    return basis function (K,)
    """
    basis1 = [] # L1-norm of the distance between the ith agent and the icecream shop
    basis2 = [] # L1-norm of the distance between the ith and jth agent
    for robotA in robots:
        basis1.append(sum([np.linalg.norm(robotA - icecream, ord=1) for icecream in icecreams]) / len(icecreams))
        for robotB in robots:
            if robotA != robotB:
                basis2.append(np.linalg.norm(robotA - robotB, ord=1))
    return basis1 + basis2

def weights(N):
    """
    weighting theta
    """
    return [1] * N