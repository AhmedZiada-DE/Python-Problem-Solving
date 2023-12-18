import math
import os
import random
import re
import sys
import time
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1 = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    seconds = int(abs(dt1 - dt2).total_seconds())
    return seconds

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(1)#input())

    for t_itr in range(t):
        t1 = "Sun 10 May 2015 13:54:36 -0700"

        t2 = "Sun 10 May 2015 13:54:36 -0000"

        delta = time_delta(t1, t2)

        # fptr.write(delta + '\n')

    #  fptr.close()
        
##########Sybmitted Solution

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1 = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    #str() is used so that we can concatenate the result with \n in this line : fptr.write(delta + '\n')
    seconds = str(int(abs(dt1 - dt2).total_seconds()))
    return seconds

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()