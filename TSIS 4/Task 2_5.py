import re
from collections import OrderedDict
od = dict()
S = input().strip()
k = input().strip()
i = 0
l = list()
if re.search(k,S) is None:
    print ((-1,-1))
else :
    while i<len(S):
        m = re.search(k,S[i:])
        if m == None:
            break;
        else:
            p = i+m.start()
            n = (p,p+len(k)-1)
            od[i] = n
        i = i+1
    for p,s in enumerate(od.values()):
        if list(od.values())[p] != list(od.values())[p - 1]:
            print(s)