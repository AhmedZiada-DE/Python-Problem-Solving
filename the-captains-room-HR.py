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


#########################################
    #Honorable Solutions from HackRank because I want to look further into them
#########################################
    
# if __name__ == "__main__":
#     K = int(input())
#     r = list(map(int, input().split()))

#     print(*set(r[1::2]).symmetric_difference(set(r[0::2])))
    
################################################################

# More compact and similar to mine
    
# from collections import Counter
# k = input()
# arr = list(map(int, input().split()))
# res = [x for x, cnt in Counter(arr).items() if cnt==1]
# print(*res)