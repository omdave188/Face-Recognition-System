import numpy as np
def pca(x):

    num_data, dim = x.shape
    mean = x.mean(axis=0)
    x = x - mean

    if dim > num_data:
        M = np.dot(x,x.T)
        e, EV = np.linalg.eigh(M)
        tmp = np.dot(x.T, EV).T
        V = tmp[::-1]
        S = np.sqrt(e[::-1])

        for i in range(V.shape[1]):
            V[:, i] /= S

    else:
        U, S, V = np.linalg.svd(x)
        V = V[:num_data]

    return V, S, mean
