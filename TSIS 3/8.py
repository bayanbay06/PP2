l, l2 = {int(i) for i in input().split()}, {int(i) for i in input().split()}
x = l.intersect(l2)
for i in x:
    print(i, end=" ")


