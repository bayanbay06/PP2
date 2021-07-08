l = [int(i) for i in input().split()]
n = l[0]
m = l[1]
a, b, counter = [], [], 0
for _ in range(n):
    a.append(int(input()))
for _ in range(m):
    b.append(int(input()))
for i in a:
    if i in b:
        counter += 1
print(counter)
z = set(a).intersection(set(b))
for i in z:
    print(i, end=" ")
print()
print(n - counter)
for i in sorted(set(a)):
    if i not in z:
        print(i, end=' ')
print()
print(m - counter)
for i in sorted(set(b)):
    if i not in z:
        print(i, end=" ")


