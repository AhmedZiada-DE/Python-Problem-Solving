# Discard, Remove and Pop numbers ranging from 0 to 9 from a set. The user specifies how many commands will be given using the cmd variable
# Then the sum of the set is printed in the end
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))
cmd = int(input())
a= 0
for i in range(cmd):
    userInp = input().split(' ')
    order = userInp[0]
    
    if order == 'remove':
        try:
            s.remove(int(userInp[1]))
        except KeyError:
            continue
    
    elif order == 'discard':
        s.discard(int(userInp[1]))
    elif order == 'pop':
        s.pop()
    a+=1
print(sum(s))



#############################################
    #Strange solution I found on HackerRank
#############################################

# n, s, N = input(), set(map(int, input().split())), int(input())
# [getattr(s,fn)(int(value[0])) if value else getattr(s,fn)() for fn,*value in [input().split() for _ in range(N)]]
# print(sum(s))