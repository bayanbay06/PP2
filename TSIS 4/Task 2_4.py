# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
element = input()
if re.findall(r'[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])', element):
    for i in re.findall(r'[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])', element):
        print(i)
else:
    print(-1)