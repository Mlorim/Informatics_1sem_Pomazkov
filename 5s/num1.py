m = [int(i) for i in input().split()]
# m = [3, 30, 34, 5, 9]
max_len = len(max([str(i) for i in m], key=len))
numbers = dict()
rez = ''

for i in range(1, 10):
    numbers[i] = []

for i in m:
    numbers[int(str(i)[0])].append(str(i))

for i in numbers:
    numbers[i].sort(key=lambda i: i + (max_len - len(i)) * i[0], reverse=True)

for i in range(9, 0, -1):
    rez += ''.join(numbers[i])

print(rez)
# Output: 9534330
