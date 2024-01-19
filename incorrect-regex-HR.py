# Checks if the regex pattern is valid or not
# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
import re
tCases = int(input())
for i in range(tCases):
    s = input()
    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)
