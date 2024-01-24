# Number of students that studied both english and french using sets and intersection

len1 = int(input())
s1 = set(map(int, input().split(' ')))
len2 = int(input())
s2 = set(map(int, input().split(' ')))

print(len(s1.intersection(s2)))