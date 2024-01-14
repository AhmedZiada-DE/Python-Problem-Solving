# Number of tests to try
testNum = int(input())
test = []
for i in range(testNum):
    li = input().split(' ')
    test.append(li)

# Input space separated values
for nums in test:
    try:
        nums = [int(num) for num in nums]
        # print in case there was no error, else show the error
        print(nums[0]//nums[1])
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as ve:
        print('Error Code:',ve)