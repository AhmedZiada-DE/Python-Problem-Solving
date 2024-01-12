# Map characters to variable lets
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
    n = 5
    print_rangoli(n)
    