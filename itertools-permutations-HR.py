# print the combinations of a string using variable num to decide the size of the output
# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations
str1, num = input().split(' ')
# options to convert str1 to separate characters not needed here though
# str1 = [x for x in str1]
# str1 = *str1
# str1 = list(str1)

num = int(num)
res = sorted(list(permutations(str1, num)))

for itr in res:
    print(''.join(itr))