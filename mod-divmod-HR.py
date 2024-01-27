# Use div mod to print the quotient and remainder

a = int(input())
b = int(input())

res = divmod(a, b)
print(res[0])
print(res[1])
print(res)