#By: Aballey Wilson

import math
import os
import random
import re
import sys

# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY and String_Array a as parameter.

 #Slicing method
def reverseArray(a):
    m = a[::-1] #Starts printing from step(-1) which is the last value
    return m

m = input()
print(reverseArray(m))

