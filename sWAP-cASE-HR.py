# The purpose of this function is to swap cases

def swap_case(s):
    # This is the first solution
    # opposite = ''
    # for letter in s:
    #     if letter == letter.lower():
    #         letter = letter.capitalize()
    #     else:
    #         letter = letter.lower()
    #     opposite+=letter
    
    # This is the second solution using a lambda function and a map
    
    opposite = ''.join(map(lambda l: l.capitalize() if l ==l.lower() else l.lower(), s))
    return opposite

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)