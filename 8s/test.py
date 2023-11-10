# ND = []
# num_mass = []
#
# while ND != [0, 0]:
#     ND = [int(i) for i in input().split()]
#     if ND != [0, 0]:
#         ND.append(int(input()))
#     num_mass.append(ND)
# num_mass = num_mass[:-1]
#
# for i in num_mass:
#
#     order = dict()
#     for s in '9876543210':
#         s = int(s)
#         order[s] = []
#
#     n = i[0]
#     d = i[1]
#     delt = n - d
#     num = str(i[2])
#     for j in range(n):
#         order[int(num[j])].append(j)
#
#     index_to_delete = []
#     for key in '0123456789':
#         index_to_delete += order[int(key)]
#
#     max1 = ''
#     for ind in range(n):
#         if ind not in index_to_delete[:d]:
#             max1 += str(num[ind])
#
#     ess_ind = dict()
#     max2 = ''
#     for key in '9876543210':
#         key = int(key)
#         if len(order[key]) != 0:
#             ind = 0
#             for i in order[key]:
#                 if n - i >= (delt - order[key][0]):
#                     ess_ind[key] = [i]
#
#     for key in '9876543210':
#         key = int(key)
#         if key in ess_ind.keys():
#             for i in order[key]:
#                 if i > ess_ind[key][-1]:
#                     ess_ind[key].append(i)

#     print(ess_ind)

f = [[1, 4], [4]]
f[0] = [5555]
print(f)
