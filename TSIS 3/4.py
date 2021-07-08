l = [int(i) for i in input().split()]
l.sort(key = lambda x: not x)
for i in l:
    print(i, end=" ")