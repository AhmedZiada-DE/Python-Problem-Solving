# You enter the number of iterations then you enter an unordered list where there are k+1 number of groups and an outsider that won't repeat in the unordered list like the rest of the group
# the number of members in each group = k
# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter
k = int(input())
ul = map(int, input().split(' '))
count = Counter(ul)

for num in count:
    if count[num] == 1:
        print(num)
        break