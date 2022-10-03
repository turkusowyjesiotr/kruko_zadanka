# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
letters = input()
k = int(input())
letters = letters.replace(' ', '')

permutations = list(combinations(letters, k))

combs = len(permutations)
contains_a = 0
for i in permutations:
    if 'a' in i:
        contains_a += 1

result = contains_a / combs
print(result)