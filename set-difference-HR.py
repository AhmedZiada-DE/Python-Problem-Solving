# Get the number of students who participated in english but didn't participate in french
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

len1 = int(input())
s1 = set(map(int, input().split(' ')))
len2 = int(input())
s2 = set(map(int, input().split(' ')))

print(len(s1.difference(s2)))

