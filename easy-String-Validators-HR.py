# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
#Check for if the string
if __name__ == '__main__':
    s = input()
    
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isnumeric, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))










###########################################
    #Great Solutions found on HackerRank
###########################################
    
# if __name__ == '__main__':
#     s = input()
#     attrs = ["isalnum", "isalpha", "isdigit", "islower", "isupper"]
#     for attr in attrs:
#         print(any(getattr(i, attr)() for i in s))
    
# print(any(i.isalnum() for i in s))
# print(any(i.isalpha() for i in s))
# print(any(i.isdigit() for i in s))
# print(any(i.islower() for i in s))
# print(any(i.isupper() for i in s))
    

# import re

# if __name__ == '__main__':
#     s = input()
#     s_alpha_num = re.sub('[^a-zA-Z0-9]','',s)
#     s_alpha = re.sub('[^a-zA-z]','',s_alpha_num)
#     s_num = re.sub("[^0-9]","",s_alpha_num)
#     s_lowercase = re.sub("[^a-z]","",s_alpha)
#     s_uppercase = re.sub("[^A-Z]","",s_alpha)

#     print((len(s_alpha_num) != 0))
#     print((len(s_alpha) != 0))
#     print((len(s_num) != 0))
#     print((len(s_lowercase) != 0))
#     print((len(s_uppercase) != 0))