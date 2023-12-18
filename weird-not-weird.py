n = int(input('Enter Input: ').strip())
if((( 1<n<5) or n > 20) and n%2==0) :
    print('Not Weird')
else:
    print('Weird')