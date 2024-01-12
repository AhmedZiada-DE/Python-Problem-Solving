# Map characters to variable lets
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
lets = list(map(chr, range(97, 123)))
def print_rangoli(size):

    for i in range(size-1,0,-1):
        # turn list to str and create the characters used in each print
        chars = ''.join(lets[i:size])
        charsToUse = '-'.join(chars[::-1] + chars[1:])
        # Center the string with dash '-' and print it
        print(charsToUse.center((size*4)-3,'-'))

    for i in range(0,size):
        chars = ''.join(lets[i:size])
        charsToUse = '-'.join(chars[::-1] + chars[1:])
        print(charsToUse.center((size*4)-3,'-'))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
########################################
    # Solutions from the discussions
########################################
    
# 1
# import string

# def print_rangoli(size: int) -> None:
#     alph = list(string.ascii_lowercase)[:size]
#     middle_line = "-".join(alph[::-1][:-1] + alph)
#     half_rangoli = ["-".join(alph[::-1][:-1*size+i-1] + alph[-1*i:]).center(len(middle_line), "-") for i in range(1, size)]
#     print("\n".join(half_rangoli + [middle_line] + half_rangoli[::-1]))
    
# 2
# import string

# def print_rangoli(size):
#     # your code goes here
#     alphabets = list(string.ascii_lowercase)
#     trans = size - 1
#     length = size * 2 - 1
#     axis = range(0 - trans, length - trans)
#     for y in axis:
#         row = [alphabets[abs(x)+abs(y)] if abs(x)+abs(y) < size else '-' for x in axis]
#         print('-'.join(row))

# 3
# for i in indices:
#     start_index = i+1
#     original = alphabet[-start_index:]
#     reverse = original[::-1]
#     row = reverse + original[1:]
#     row = '-'.join(row)
#     width = size*4-3
#     row = row.center(width,'-')
#     print(row)
     
# 4
# alp = "abcdefghijklmnopqrstuvwxyz";
# def print_rangoli(size):
#     n_rows = 2 * size - 1
#     for i in range(n_rows):
#         letters = alp[abs(size - i - 1): size]
#         dashed_letters = "-".join(letters[::-1][:-1]+letters)
#         print(dashed_letters.center((4*size-3),"-"))