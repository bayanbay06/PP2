l, l2, counter = [int(i) for i in input().split()], [int(i) for i in input().split()], 0
for i in l:
    if i in l2:
        counter += 1
print(counter)


