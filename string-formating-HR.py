# This function takes a number and prints its variations (decimal, octal, hexa and binary) and it also pads each number to the right
def print_formatted(number):
    leng = len(bin(number)[2:])
    for i in range(1,number+1):
        dec = str(i).rjust(leng,' '),           #Could have used .rjust(col_size) or .rjust(adj_size)
        octa = oct(i)[2:].rjust(leng,' '),
        hexa = hex(i)[2:].upper().rjust(leng,' '),  
        bina = bin(i)[2:].rjust(leng,' ')
        print(dec, octa, hexa, bina)


if __name__ == '__main__':
    n = 15
    print_formatted(n)