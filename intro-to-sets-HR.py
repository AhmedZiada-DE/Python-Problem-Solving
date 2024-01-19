# Calculate the average of the distinct values entered from the space separated integers entered in the var arr
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    nums = set(array)
    res = round(sum(nums)/len(nums),3)
    return res
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)