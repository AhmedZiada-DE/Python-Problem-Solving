# The number of students who participated in only one course and not both
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
n1 = int(input())
s1 = set(input().split(' '))
n2 = int(input())
s2 = set(input().split(' '))
print(len(s1.difference(s2))+len(s2.difference(s1)))