# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

data = input()
group_length = []
uniquekeys = []
for k, g in groupby(data):
    group_length.append(len(list(g)))
    uniquekeys.append(int(k))

zipped = tuple(zip(group_length, uniquekeys))
result = ' '.join(str(i) for i in zipped)
print(result)
