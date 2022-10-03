# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n = int(input())
words = []
for i in range(n):
    j = input()
    words.append(j)

# normal dictionary solution
# c = {}
# for word in words:
#     if word not in c.keys():
#         c[word] = 0
#     c[word] += 1

# Counter solution
c = Counter()
for word in words:
    c[word] += 1

distinct_words = len(c.keys())
occurrences = ' '.join(str(v) for v in c.values())

print(distinct_words)
print(occurrences)
