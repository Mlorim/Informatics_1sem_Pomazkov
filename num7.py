f = input().split(" ")
max_i = 0
max_cont = 0
for i in f:
    if f.count(i) >= max_cont:
        max_cont = f.count(i)
        max_i = i
print(max_i)