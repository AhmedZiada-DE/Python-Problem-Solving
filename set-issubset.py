# Checks a number of times t if set s1 is a subset of set s2
t = int(input())
for i in range(t):
    length1 = int(input())
    s1 = set(input().split(' '))
    length2 = int(input())
    s2 = set(input().split(' '))
    print(s1.issubset(s2))
    # if len(s1.difference(s2)) == 0:
        # print(True)
    # else:
        # print(False)
