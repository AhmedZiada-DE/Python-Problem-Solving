# lst = [['Harsh',20], ['Beria',20], ['Varum',19], ['Kakunami',19], ['Vikas',21]]
# 
# Main Solution
# if __name__ == '__main__':
    # lst = []
    # for _ in range(int(input())):
        # name = input()
        # score = float(input())
        # lst.append([name, score])
# 
    # numOnce = [x[1] for x in lst]
    # numOnce = list(set(numOnce))
    # numOnce.sort()
    # lst2=[]
    # if len(numOnce)>1:
        # i=1
    # else:
        # i=0
    # a=True
    # while True:
        # 
        # for num in lst:
            # if num[i] == numOnce[i] :
                # lst2.append(num)
                # a=False
                # 
        # if a is False:
            # break
        # else:
            # i+=1
    # 
    # 
    # lst2 = sorted(lst2, key=lambda x: x[0])
    # for name in lst2:
        # print(name[0])
            
# BEST Solution
if __name__ == '__main__':
    # reords = []
    reords = [['Harsh',20], ['Beria',20], ['Varum',19], ['Kakunami',19], ['Vikas',21]]
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     reords.append([name, score])

    mark = sorted(set(map(lambda x: x[1], reords)))
    print(mark)
    mark = sorted(set(map(lambda x: x[1], reords)))[1]
    print(mark)
    for n, m in sorted(filter(lambda x: x[1] == mark, reords)):
        print(n)
