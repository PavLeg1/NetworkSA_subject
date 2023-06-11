# from multiprocessing import Pool
#
#
# def matmul_helper(tup):
#     i, j, matrixA, matrixB = tup
#     return sum([matrixA[i][k] * matrixB[k][j] for k in range(len(matrixB))])
#
#
# if __name__ == "__main__":
#     # Define matrices as arrays of arrays
#     matrixA = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     matrixB = [
#         [1, 2],
#         [3, 4],
#         [5, 6]
#     ]
#
#     # Get matrix dimensions
#     m, n = len(matrixA), len(matrixA[0])
#     p, q = len(matrixB), len(matrixB[0])
#
#     if n != p:
#         raise ValueError("Matrices cannot be multiplied: mismatched dimensions.")
#
#     # Create result matrix
#     res = [[0 for j in range(q)] for i in range(m)]
#
#     # Create pool of worker processes
#     with Pool() as pool:
#         # Create list of index tuples to be processed
#         indices = [(i, j, matrixA, matrixB) for i in range(m) for j in range(q)]
#         # Calculate results using pool.map()
#         results = pool.map(matmul_helper, indices)
#
#     # Assign results to the result matrix
#     for i, j, _, _ in indices:
#         res[i][j] = results.pop(0)
#
#     # Print result matrix
#     for row in res:
#         print(row)

from multiprocessing import Pool
import numpy as np
import os

def matmul_helper(tup, matrixA, matrixB):
    i, j = tup
    return sum([matrixA[i][k] * matrixB[k][j] for k in range(len(matrixB))])

if __name__ == "__main__":
    # read matrices from files
    matrixA = np.loadtxt("matrixA.txt")
    matrixB = np.loadtxt("matrixB.txt")

    if not os.path.exists("matrixB.txt") or not os.path.exists("matrixB.txt"):
        raise ValueError("File with matrix cannot be found.")

    # get matrix dimensions
    m, n = matrixA.shape
    p, q = matrixB.shape

    if n != p:
        raise ValueError("Matrices cannot be multiplied: mismatched dimensions.")

    # create result matrix
    res = np.zeros((m, q))

    # create pool of worker processes
    with Pool() as pool:
        # create list of index tuples to be processed
        indices = [(i, j) for i in range(m) for j in range(q)]
        # calculate results using pool.map()
        results = pool.starmap(matmul_helper, [(idx, matrixA, matrixB) for idx in indices])

    # reshape and save results
    res = np.reshape(results, (m, q))
    np.savetxt("result.txt", res)
    print(np.loadtxt("result.txt"))

