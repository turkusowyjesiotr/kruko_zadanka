# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

n = int(input())
shoes = input().split()
c = Counter(shoes)
customers = int(input())
earned = 0
for customer in range(customers):
    size, price = input().split()
    if size in c and c[size] != 0:
        earned += int(price)
        c[size] -= 1

print(earned)