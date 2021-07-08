l = [int(i) for i in input().split()]
n = int(input())
for i in l[n:] + l[:n]:
    print(i, end=" ")


