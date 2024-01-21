# Check if s1 is a superset of s2
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

s1 = set(input().split(' '))
N = int(input())
res = True
for i in range(N):
    s2 = set(input().split(' '))
    # if s1.issuperset(s2):
    if len(s2.difference(s1)) == 0 and len(s1.difference(s2))>0:
        pass
    else:
        res = False
        break
print(res)