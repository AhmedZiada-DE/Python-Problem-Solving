# This loop listens for commands on a list and simply runs the commands
if __name__ == '__main__':
    N = int(input())
    li = []

    for i in range(N):
        inp = input()
        inp = inp.split(' ')

        #Commands without providing numbers
        if len(inp) == 1:
            if inp[0] == 'print':
                print(li)
            elif inp[0]=='sort':
                li.sort()
            elif inp[0]=='pop':
                li.pop()
            elif inp[0]=='reverse':
                li.reverse()

        # Commands that have to provide numbers
        elif len(inp)>1 :
            inp1 = int(inp[1])
            if inp[0] == 'insert':
                li.insert( inp1 , int(inp[2]))
            elif inp[0]=='append':
                li.append(int(inp[1]))
            elif inp[0] == 'remove':
                li.remove(inp1)
                
                