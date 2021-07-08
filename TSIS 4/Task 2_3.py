def firstRepeatedChar(s):
    return next((j for j, i in zip(s, s[1:]) if j == i and j.isalnum()), -1)

q = input()

print(firstRepeatedChar(q))


