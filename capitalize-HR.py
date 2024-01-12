# Capitalize the first letter in Each word
# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
import math
import os
import random
import re
import sys

def solve(s):
    name = ' '.join(map(str.capitalize, s.split(' ')))
    return name
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()