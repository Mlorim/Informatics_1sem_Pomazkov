set_1 = {int(i) for i in input().split()}
set_2 = {int(i) for i in input().split()}

union = set_1 | set_2
intersection = set_1 & set_2

print(*set_1)
print(*set_2)
print(*union)

if len(intersection) == 0:
    print('-')
else:
    print(*intersection)
