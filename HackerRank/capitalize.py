#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
s = "ayesha siddika"
s1 = [word.capitalize() for word in s.split(' ')]
print(' '.join(s1))




s = [s[c].upper() if (c-1 >= 0 and (s[c-1] == ' ')) or c == 0 else s[c] for c in range(len(s))]
print(''.join(s))



#print ' '.join(word.capitalize() for word in raw_input().split(' '))




"""

"""