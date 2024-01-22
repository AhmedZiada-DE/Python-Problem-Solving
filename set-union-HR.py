# Print the number ofstudents who participated in at least one course or more
# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
n1 = int(input())
s1 = set(input().split(' '))
n2 = int(input())
s2 = set(input().split(' '))
print(len(s1.union(s2)))