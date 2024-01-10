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


#########################################################################
    #    Another Solutions that uses center
#########################################################################
       
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# if __name__ == "__main__":
#     # Get n and m dimensions from stdin
#     n, m = map(int, input().split())
    
#     # Build top half of the mat
#     # Line before welcome always has n-2 .|. patterns.
#     # Since strings start at 0, our range end is n-1.
#     # We start with 1 .|. and each row has 2 more
#     # Until we reach the line before welcome.
#     # center() surrounds our .|. with - on either side
#     # until the strlen is of length m.
#     for i in range(1, n-1, 2):
#         print((".|."*i).center(m, "-"))
    
#     # Always print welcome and surround either side with -
#     # until strlen == m
#     print("WELCOME".center(m, "-"))
    
#     # Build bottom half of the mat
#     # Line after welcome always has n-2 .|. patterns.
#     # Since strings start at 0, but we're in the bottom half
#     # our range end is 0 and our start is n-2.
#     # We start with n-2 .|. and each row has 2 less
#     # Until we reach the last line of the mat.
#     # center() surrounds our .|. with - on either side
#     # until the strlen is of length m.
#     for j in range(n-2, 0, -2):
#         print((".|."*j).center(m, "-"))
       
# SECOND Solution

# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     half_mat = [(".|."*(1+2*i)).center(M, "-") for i in range(N) if i < int(N/2)]
#     print("\n".join(half_mat + ["WELCOME".center(M, "-")] + half_mat[::-1]))