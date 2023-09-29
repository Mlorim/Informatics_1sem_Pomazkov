import numpy as np

a = np.array([[1,2,3], [5,6,7], [1,10,11]])
b = np.array([[0], [4], [7]])
# delts = []
# for i in range(1,a.shape[1]+1):
#     i_mat = a[:, :i-1]
#     i_mat = np.hstack((i_mat,b))
#     rest = a[:, i:]
#     i_mat = np.hstack((i_mat,rest))
#     delts.append(round(np.linalg.det(i_mat), 10))
# print(delts)

print(a[:, -1:])

# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(a[:, :1-1])
# print(a[:, 1:])

