# Inputing two space separated values the first is higher than 5 and the second must be treble the first
nums = input()
nums = nums.split(' ')
N = int(nums[0])
M = int(nums[1])

# Ensuring that the input matches the condition given
if N>5 and N % 2 != 0 and N*3 == M:
    # Printing the top layer of the mat
    for i in range(1,N,2):
       filler = int((M-(i*3))/2)
       print('-'*filler + '.|.'*i + '-'*filler) 
    # Printing the Welcome message
    print('-'*((M-7)//2) + 'WELCOME' + '-'*((M-7)//2))
    # Reversing the first loop to make the bottom layer
    for i in reversed(range(1,N,2)):
       filler = int((M-(i*3))/2)
       print('-'*filler + '.|.'*i + '-'*filler) 
