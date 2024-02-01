# print the combinations of a string using variable num to decide the size of the output
# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
from itertools import permutations
str1, num = input().split(' ')
str1 = [x for x in str1]
# Other options to convert str1 to separate characters
# str1 = *str1
# str1 = list(str1)
# print(str1)
num = int(num)
res = list(permutations(str1, num))
lst = []
for itr in res:
    lst.append(''.join(itr))

lst.sort()
for item in lst:
    print(item)