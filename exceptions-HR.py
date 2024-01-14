testNum = int(input())
test = []
for i in range(testNum):
    li = input().split(' ')
    test.append(li)
    
for nums in test:
    try:
        nums = [int(num) for num in nums]
        print(nums[0]//nums[1])
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as ve:
        print('Error Code:',ve)