# Find the numbers that exist in set m and doesn't exist in n. Then do the same with n. and print the numbers in a sorted order
# print each number in separate line
# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
mLen = int(input())
m = set(map(int, input().split()))

nLen = int(input())
n = set(map(int, input().split()))

li = []
li.extend(m.difference(n))
li.extend(n.difference(m))
li.sort()
for item in li:
    print(item)