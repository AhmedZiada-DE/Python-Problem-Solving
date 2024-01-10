# The purpose of this code is to get the cartesian product of 2 inputs
from itertools import product

a = map(int, input().split(' '))
b = map(int, input().split(' '))

# The astrix * is for unpacking the list so that it can appear without the brackets
print(*list(product(a,b)))