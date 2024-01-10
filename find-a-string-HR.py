# The purpose of the code is to find how many times a substring occured in a string
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    counter = 0
    subsLength = len(sub_string)
    for i in range(len(string)):
        if sub_string == string[i:i+ subsLength]:
            counter+=1
    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)