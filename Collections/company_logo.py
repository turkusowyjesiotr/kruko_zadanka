# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    s = sorted(s)
    c = Counter(s).most_common(3)
    for el in c:
        print(str(el[0]) + ' ' + str(el[1]))

