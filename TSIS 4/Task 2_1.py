import re
num = int(input())
for _ in range(num):
    element = input()
    if re.match(r'^-?\d+(?:\.\d+)$', element):
        print(True)
    elif re.match(r'^\+?\d+(?:\.\d+)$', element):
        print(True)
    elif re.match(r'^\+?(?:\.\d+)$', element):
        print(True)
    else:
        print(False)


