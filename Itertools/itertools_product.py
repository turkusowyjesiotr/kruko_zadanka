# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(input().split())
b = list(input().split())
a = [int(i) for i in a]
b = [int(i) for i in b]

prod = list(product(a, b))
result = ' '.join([str(i) for i in prod])
print(result)