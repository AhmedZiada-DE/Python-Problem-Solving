def minion_game(string):
    # your code goes here
    stuartPoints = kevinPoints = 0
    vowels = 'AEIOU'
    strLength = len(string)
    # for i in range(strLength):
    #     if string[i] in vowels:
    #         kevinPoints+=(strLength-i)
    #     else:
    #         stuartPoints+=(strLength-i)
    
    # if kevinPoints>stuartPoints:
    #     print(f"Kevin {kevinPoints}")
    # elif stuartPoints>kevinPoints:
    #     print(f"Stuart {stuartPoints}")
    # else:
    #     print('Draw')

    # Another solution by iterating each possible substring
    for i in range(strLength):
        for j in range(i,strLength):
            stringComb = string[i:j+1]
            if stringComb[0] in vowels:
                kevinPoints+=1
            else:
                stuartPoints+=1
    
    if kevinPoints>stuartPoints:
        print(f"Kevin {kevinPoints}")
    elif stuartPoints>kevinPoints:
        print(f"Stuart {stuartPoints}")
    else:
        print('Draw')
    print(kevinPoints, 'Kevin')
    print(stuartPoints, 'Stuart')
            
if __name__ == '__main__':
    s = input()
    minion_game(s)