# Print the hash values of space separated integerts after turning them into a tuple
from builtins import hash
iterations = int(input())
t = tuple(map(int, input().split(' ')))

print(hash(t))
