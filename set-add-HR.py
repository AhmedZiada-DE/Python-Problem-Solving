# Add to set for a number of times n and print the length

n = int(input())
countries = set()
for i in range(n):
    countries.add(input())
    
print(len(countries))