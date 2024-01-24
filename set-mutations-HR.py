# Give commands to a set of integers and sum the set in the end
# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

s1Len = int(input())
s1 = set(map(int, input().split(' ')))
numOfCommands = int(input())

for i in range(numOfCommands):
    comm = input().split(' ')
    enter = set(map(int, input().split(' ')))
    if comm[0] == 'intersection_update':
        s1.intersection_update(enter)
    elif comm[0] == 'update':
        s1.update(enter)
    elif comm[0] == 'symmetric_difference_update':
        s1.symmetric_difference_update(enter)
    elif comm[0] == 'difference_update':
        s1.difference_update(enter)

print(sum(s1))