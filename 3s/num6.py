import numpy as np


def LESolver(n, m):
    ext_mat = []
    for i in range(n):
        for j in [int(i) for i in input().split()]:
            ext_mat.append(j)
    ext_mat = np.array(ext_mat).reshape((n, m))

    if n != (m - 1):
        print("It can't be solved this way!")
    else:
        main_mat = ext_mat[:, :m - 1]
        delt = round(np.linalg.det(main_mat), 10)
        results = ext_mat[:, -1:]

        if delt == 0:
            print("The number of solutions is zero or infinity.")
        else:
            delts = []
            for i in range(1, n + 1):
                i_mat = main_mat[:, :i - 1]
                i_mat = np.hstack((i_mat, results))
                rest = main_mat[:, i:]
                i_mat = np.hstack((i_mat, rest))
                delts.append(round(np.linalg.det(i_mat), 10))

            return [delts[i]/delt for i in range(len(delts))]


print(LESolver(3, 4))
